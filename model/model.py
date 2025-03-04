import torch.nn as nn
import torch.nn.functional as F
from utils.utils import get_configs


class Neural_Net(nn.Module):
    def __init__(self, input_size, num_classes):
        super(Neural_Net, self).__init__()
        self.fc1 = nn.Linear(input_size, 256)
        self.fc2 = nn.Linear(256, num_classes)

    def forward(self, x):
        _x = F.relu(self.fc1(x))
        out = self.fc2(_x)

        return out
