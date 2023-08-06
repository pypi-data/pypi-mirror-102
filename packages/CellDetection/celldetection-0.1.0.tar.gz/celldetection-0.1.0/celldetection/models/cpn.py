from ..util.util import lookup_nn
import torch
import torch.nn as nn
from torch import Tensor
import torch.nn.functional as F
from collections import OrderedDict
from typing import List, Union, Dict, Tuple
from ..util.util import add_to_loss_dict, reduce_loss_dict, fetch_model
from ..ops.commons import downsample_labels
from ..ops.cpn import rel_location2abs_location, fourier2contour, scale_contours, scale_fourier, batched_box_nms, \
    order_weighting


class ReadOut(nn.Module):
    def __init__(
            self,
            channels_in,
            channels_out,
            kernel_size=3,
            padding=1,
            activation='relu',
            norm='batchnorm2d',
            final_activation=None,
            dropout=0.1,
            channels_mid=None,
            stride=1
    ):
        super().__init__()
        self.channels_out = channels_out
        if channels_mid is None:
            channels_mid = channels_in

        self.block = nn.Sequential(
            nn.Conv2d(channels_in, channels_mid, kernel_size, padding=padding, stride=stride),
            lookup_nn(norm, channels_mid),
            lookup_nn(activation),
            nn.Dropout2d(p=dropout) if dropout else nn.Identity(),
            nn.Conv2d(channels_mid, channels_out, 1),
        )

        if final_activation is ...:
            self.activation = lookup_nn(activation)
        else:
            self.activation = lookup_nn(final_activation)

    def forward(self, x):
        out = self.block(x)
        return self.activation(out)


class CPNCore(nn.Module):
    def __init__(
            self,
            backbone: nn.Module,
            backbone_channels,
            order,
            score_channels: int,
            refinement: bool = True,
            refinement_margin: float = 3.,
            contour_features='1',
            refinement_features='0',
            contour_head_channels=None,
            contour_head_stride=1,
            refinement_head_channels=None,
            refinement_head_stride=1,
            refinement_interpolation='bilinear'
    ):
        super().__init__()
        self.order = order
        self.backbone = backbone
        self.refinement_features = refinement_features
        self.contour_features = contour_features
        self.refinement_interpolation = refinement_interpolation
        if isinstance(backbone_channels, int):
            contour_head_input_channels = refinement_head_input_channels = backbone_channels
        elif isinstance(backbone_channels, (tuple, list)):
            contour_head_input_channels = backbone_channels[int(contour_features)]
            refinement_head_input_channels = backbone_channels[int(refinement_features)]
        elif isinstance(backbone_channels, dict):
            contour_head_input_channels = backbone_channels[contour_features]
            refinement_head_input_channels = backbone_channels[refinement_features]
        else:
            raise ValueError('Did not understand type of backbone_channels')
        self.score_head = ReadOut(
            contour_head_input_channels, score_channels,
            kernel_size=3,
            padding=1,
            channels_mid=contour_head_channels,
            stride=contour_head_stride
        )
        self.score_logsoft = nn.LogSoftmax(dim=1) if score_channels == 2 else nn.Identity()
        self.location_head = ReadOut(
            contour_head_input_channels, 2,
            kernel_size=7,
            padding=3,
            channels_mid=contour_head_channels,
            stride=contour_head_stride
        )
        self.fourier_head = ReadOut(
            contour_head_input_channels, order * 4,
            kernel_size=7,
            padding=3,
            channels_mid=contour_head_channels,
            stride=contour_head_stride
        )
        if refinement:
            self.refinement_head = ReadOut(
                refinement_head_input_channels, 2,
                kernel_size=7,
                padding=3,
                final_activation='tanh',
                channels_mid=refinement_head_channels,
                stride=refinement_head_stride
            )
            self.refinement_margin = refinement_margin
        else:
            self.refinement_head = None
            self.refinement_margin = None

    def forward(self, inputs):
        features = self.backbone(inputs)
        if isinstance(features, torch.Tensor):
            contour_features = refinement_features = features
        else:
            contour_features = features[self.contour_features]
            refinement_features = features[self.refinement_features]
        scores = self.score_head(contour_features)
        locations = self.location_head(contour_features)
        fourier = self.fourier_head(contour_features)

        refinement = None
        if self.refinement_head is not None:
            refinement = self.refinement_head(refinement_features) * self.refinement_margin
            if refinement.shape[-2:] != inputs.shape[-2:]:  # 337 ns
                # bilinear: 3.79 ms for (128, 128) to (512, 512)
                # bicubic: 11.5 ms for (128, 128) to (512, 512)
                refinement = F.interpolate(refinement, inputs.shape[-2:],
                                           mode=self.refinement_interpolation, align_corners=False)
        return scores, locations, refinement, fourier


class CPN(nn.Module):
    def __init__(
            self,
            backbone: nn.Module,
            order: int = 5,
            nms_thresh: float = .2,
            score_thresh: float = .5,
            samples: int = 32,
            classes: int = 2,

            refinement: bool = True,
            refinement_iterations: int = 4,
            refinement_margin: float = 3.,
            contour_features='1',
            refinement_features='0',

            contour_head_channels=None,
            contour_head_stride=1,
            order_weights=True,
            refinement_head_channels=None,
            refinement_head_stride=1,
            refinement_interpolation='bilinear'
    ):
        """

        References:
            https://arxiv.org/abs/2104.03393

        Args:
            backbone:
            order:
            nms_thresh:
            score_thresh:
            samples:
            classes:
            refinement:
            refinement_iterations:
            refinement_margin:
            contour_features:
            refinement_features:
            contour_head_channels:
            contour_head_stride:
            order_weights:
            refinement_head_channels:
            refinement_head_stride:
            refinement_interpolation:
        """

        super().__init__()
        self.order = order
        self.nms_thresh = nms_thresh
        self.samples = samples
        self.score_thresh = score_thresh
        self.score_channels = classes
        self.refinement = refinement
        self.refinement_iterations = refinement_iterations
        self.refinement_margin = refinement_margin
        self.functional = False
        self.full_detail = False

        if not hasattr(backbone, 'out_channels'):
            raise ValueError('Backbone should have an attribute out_channels that states the channels of its output.')

        self.core = CPNCore(
            backbone=backbone,
            backbone_channels=backbone.out_channels,
            order=order,
            score_channels=classes,
            refinement=refinement,
            refinement_margin=refinement_margin,
            contour_features=contour_features,
            refinement_features=refinement_features,
            contour_head_channels=contour_head_channels,
            contour_head_stride=contour_head_stride,
            refinement_head_channels=refinement_head_channels,
            refinement_head_stride=refinement_head_stride,
            refinement_interpolation=refinement_interpolation
        )

        self.order_weights = 1.
        if isinstance(order_weights, bool):
            if order_weights:
                self.order_weights = nn.Parameter(order_weighting(self.order), requires_grad=False)
        else:
            self.order_weights = order_weights

        self.objectives = OrderedDict({
            'score': nn.CrossEntropyLoss(),
            'fourier': nn.L1Loss(reduction='none'),
            'location': nn.L1Loss(),
            'contour': nn.L1Loss(),
            'refinement': nn.L1Loss(),
            'boxes': nn.L1Loss()
        })
        self.weights = {
            'fourier': 1.,  # note: fourier has order specific weights
            'location': 1.,
            'contour': 3.,
            'score': 1.,
            'refinement': 1.,
            'boxes': .88
        }

        self._rel_location2abs_location_cache: Dict[str, Tensor] = {}
        self._fourier2contour_cache: Dict[str, Tensor] = {}

    def compute_loss(
            self,
            fourier,
            locations,
            contours,
            refined_contours,
            boxes,
            raw_scores,
            targets: dict,
            labels,
            fg_masks,
            b
    ):
        assert targets is not None

        fourier_targets = targets.get('fourier')
        location_targets = targets.get('locations')
        contour_targets = targets.get('sampled_contours')
        hires_contour_targets = targets.get('hires_sampled_contours')
        box_targets = targets.get('boxes')
        class_targets = targets.get('classes')

        losses = OrderedDict({
            'fourier': None,
            'location': None,
            'contour': None,
            'score': None,
            'refinement': None,
            'boxes': None
        })

        bg_masks = labels == 0
        fg_n, fg_y, fg_x = torch.where(fg_masks)
        bg_n, bg_y, bg_x = torch.where(bg_masks)
        objectives = self.objectives

        fg_scores = raw_scores[fg_n, :, fg_y, fg_x]  # Tensor[-1, classes]
        bg_scores = raw_scores[bg_n, :, bg_y, bg_x]  # Tensor[-1, classes]
        fg_indices = labels[fg_n, fg_y, fg_x].long() - 1  # -1 because fg labels start at 1, but indices at 0

        if fg_scores.numel() > 0:
            if class_targets is None:
                ones = torch.broadcast_tensors(torch.ones((), dtype=torch.int64, device=fg_scores.device),
                                               fg_scores[..., 0])[0]
            else:
                ones = class_targets[b, fg_indices]
            add_to_loss_dict(losses, 'score', objectives['score'](fg_scores, ones), self.weights['score'])
        if bg_scores.numel() > 0:
            zeros = torch.broadcast_tensors(torch.zeros((), dtype=torch.int64, device=bg_scores.device),
                                            bg_scores[..., 0])[0]
            add_to_loss_dict(losses, 'score', objectives['score'](bg_scores, zeros), self.weights['score'])

        if fg_indices.numel() > 0:
            if fourier_targets is not None:
                f_tar = fourier_targets[b, fg_indices]  # Tensor[num_pixels, order, 4]
                add_to_loss_dict(losses, 'fourier',
                                 (objectives['fourier'](fourier, f_tar) * self.order_weights).mean(),
                                 self.weights['fourier'])
            if location_targets is not None:
                l_tar = location_targets[b, fg_indices]  # Tensor[num_pixels, 2]
                assert len(locations) == len(l_tar)
                add_to_loss_dict(losses, 'location',
                                 objectives['location'](locations, l_tar),
                                 self.weights['location'])
            if contour_targets is not None:
                c_tar = contour_targets[b, fg_indices]  # Tensor[num_pixels, samples, 2]
                add_to_loss_dict(losses, 'contour',
                                 objectives['contour'](contours, c_tar),
                                 self.weights['contour'])

                if self.refinement and self.refinement_iterations > 0:
                    if hires_contour_targets is None:
                        cc_tar = c_tar
                    else:
                        cc_tar = hires_contour_targets[b, fg_indices]  # Tensor[num_pixels, samples', 2]

                    add_to_loss_dict(losses, 'refinement',
                                     objectives['refinement'](refined_contours, cc_tar),
                                     self.weights['refinement'])
            elif box_targets is not None:
                b_tar = box_targets[b, fg_indices]  # Tensor[num_pixels, 4]
                add_to_loss_dict(losses, 'boxes',
                                 objectives['boxes'](boxes, b_tar),
                                 self.weights['boxes'])
        loss = reduce_loss_dict(losses, 1)
        return loss, losses

    def forward(
            self,
            inputs,
            targets: Dict[str, Tensor] = None,
            nms=True
    ):
        # Presets
        original_size = inputs.shape[-2:]

        # Core
        scores, locations, refinement, fourier = self.core(inputs)

        # Scores
        raw_scores = scores
        if self.score_channels == 1:
            classes = torch.squeeze((scores > self.score_thresh).long(), 1)
        elif self.score_channels == 2:
            scores = F.softmax(scores, dim=1)[:, 1:2]
            classes = torch.squeeze((scores > self.score_thresh).long(), 1)
        elif self.score_channels > 2:
            scores = F.softmax(scores, dim=1)
            classes = torch.argmax(scores, dim=1).long()
        else:
            raise ValueError

        actual_size = fourier.shape[-2:]
        n, c, h, w = fourier.shape
        if self.functional:
            fourier = fourier.view((n, c // 2, 2, h, w))
        else:
            fourier = fourier.view((n, c // 4, 4, h, w))

        # Maybe apply changed order
        if self.order < self.core.order:
            fourier = fourier[:, :self.order]

        # Fetch sampling and labels
        if self.training:
            if targets is None:
                raise ValueError("In training mode, targets should be passed")
            sampling = targets.get('sampling')
            labels = targets['labels']
        else:
            sampling = None
            labels = classes.detach()
        labels = downsample_labels(labels[:, None], actual_size)[:, 0]

        # Locations
        # raw_locations = locations.detach()
        locations = rel_location2abs_location(locations, cache=self._rel_location2abs_location_cache)

        # Extract proposals
        fg_mask = labels > 0
        b, y, x = torch.where(fg_mask)
        selected_fourier = fourier[b, :, :, y, x]  # Tensor[-1, order, 4]
        selected_locations = locations[b, :, y, x]  # Tensor[-1, 2]
        selected_classes = classes[b, y, x]

        if self.score_channels in (1, 2):
            selected_scores = scores[b, 0, y, x]  # Tensor[-1]
        elif self.score_channels > 2:
            selected_scores = scores[b, selected_classes, y, x]  # Tensor[-1]
        else:
            raise ValueError

        if sampling is not None:
            sampling = sampling[b]

        # Convert to pixel space
        selected_contour_proposals = fourier2contour(selected_fourier, selected_locations,
                                                     samples=self.samples, sampling=sampling,
                                                     cache=self._fourier2contour_cache)

        # Rescale in case of multi-scale
        selected_contour_proposals = scale_contours(actual_size=actual_size, original_size=original_size,
                                                    contours=selected_contour_proposals)
        selected_fourier, selected_locations = scale_fourier(actual_size=actual_size, original_size=original_size,
                                                             fourier=selected_fourier, location=selected_locations)

        if self.refinement and self.refinement_iterations > 0:
            det_indices = selected_contour_proposals  # Tensor[num_contours, samples, 2]
            num_loops = self.refinement_iterations
            if self.training and num_loops > 1:
                num_loops = torch.randint(low=1, high=num_loops + 1, size=())

            for _ in torch.arange(0, num_loops):
                det_indices = torch.round(det_indices.detach())
                det_indices[..., 0].clamp_(0, original_size[1] - 1)
                det_indices[..., 1].clamp_(0, original_size[0] - 1)
                indices = det_indices.detach().long()  # Tensor[-1, samples, 2]
                responses = refinement[b[:, None], :, indices[:, :, 1], indices[:, :, 0]]  # Tensor[-1, samples, 2]
                det_indices = det_indices + responses
            selected_contours = det_indices
        else:
            selected_contours = selected_contour_proposals

        # Bounding boxes
        if selected_contours.numel() > 0:
            selected_boxes = torch.cat((selected_contours.min(1).values,
                                        selected_contours.max(1).values), 1)  # 43.3 µs ± 290 ns for Tensor[2203, 32, 2]
        else:
            selected_boxes = torch.empty((0, 4), device=selected_contours.device)

        # Loss
        if self.training:
            loss, losses = self.compute_loss(
                fourier=selected_fourier,
                locations=selected_locations,
                contours=selected_contour_proposals,
                refined_contours=selected_contours,
                boxes=selected_boxes,
                raw_scores=raw_scores,
                targets=targets,
                labels=labels,
                fg_masks=fg_mask,
                b=b
            )
        else:
            loss, losses = None, None

        if self.training and not self.full_detail:
            return OrderedDict({
                'loss': loss,
                'losses': losses,
            })

        final_contours = []
        final_boxes = []
        final_scores = []
        final_classes = []
        final_locations = []
        final_fourier = []
        final_contour_proposals = []
        for batch_index in range(inputs.shape[0]):
            sel = b == batch_index
            final_contours.append(selected_contours[sel])
            final_boxes.append(selected_boxes[sel])
            final_scores.append(selected_scores[sel])
            final_classes.append(selected_classes[sel])
            final_locations.append(selected_locations[sel])
            final_fourier.append(selected_fourier[sel])
            final_contour_proposals.append(selected_contour_proposals[sel])

        if not self.training and nms:
            nms_r = batched_box_nms(
                final_boxes, final_scores, final_contours, final_locations, final_fourier, final_contour_proposals, final_classes,
                iou_threshold=self.nms_thresh
            )
            final_boxes, final_scores, final_contours, final_locations, final_fourier, final_contour_proposals, final_classes = nms_r

        # The dict below can be altered to return additional items of interest
        outputs = OrderedDict({
            'contours': final_contours,
            'boxes': final_boxes,
            'scores': final_scores,
            'classes': final_classes,
            'loss': loss,
            'losses': losses,
        })

        return outputs


models_by_name = {
    'cpn_u22': 'cpn_u22'
}


def get_cpn(name):
    return fetch_model(models_by_name[name])
