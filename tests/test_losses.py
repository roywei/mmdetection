import torch
import numpy as np

def test_giou():
    from mmdet.models.losses.iou_loss import giou_loss
    giou_loss(np.zeros((1,10,4)), np.zeros((1,10,4)))