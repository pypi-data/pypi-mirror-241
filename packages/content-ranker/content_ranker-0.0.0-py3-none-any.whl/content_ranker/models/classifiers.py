"""
‫این ماژول شبکه ی bidirectional lstm crf را برای classification در بر دارد.
"""

import random
import sys

import numpy as np
import torch
import torch.nn as nn

from content_ranker.models.crf import CRF


class LeafClassifier(nn.Module):
    def __init__(self, input_dim, dense_size, hid_dim, num_layer, num_classes, dropout, seed):
        super().__init__()
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed(seed)
        torch.backends.cudnn.deterministic = True

        self.fc1 = nn.Linear(input_dim, dense_size)

        self.relu = nn.ReLU()

        self.rnn = nn.LSTM(dense_size, hid_dim, num_layers=num_layer, bidirectional=True)

        self.dropout = nn.Dropout(dropout)

        self.crf = CRF(2 * hid_dim, num_classes)

    def __build_features(self, src):
        masks = torch.sum(src, dim=2).gt(0)

        masks = masks.permute(1, 0)

        x = self.fc1(src)

        x = self.relu(x)

        x, _ = self.rnn(x)

        x = self.dropout(x)

        x = x.permute(1, 0, 2)

        return x, masks

    def forward(self, src):
        features, masks = self.__build_features(src)

        scores, tag_seq = self.crf(features, masks)

        return scores, tag_seq

    def loss(self, src, tags):
        features, masks = self.__build_features(src)
        loss = self.crf.loss(features, tags, masks=masks)
        return loss
