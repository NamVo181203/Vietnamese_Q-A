import os
import torchvision.datasets as datasets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split
import pytorch_lightning as pl

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'


class MnistDataModule(pl.LightningDataModule):
    def __init__(self, conf):
        super().__init__()
        self.conf = conf
        self.test_ds = None
        self.train_ds = None
        self.val_ds = None

    def prepare_data(self):
        # Download data from cloud
        pass

    def setup(self, stage: str) -> None:
        # stage: either ``'fit'``, ``'validate'``, ``'test'``, or ``'predict'``
        if stage == "fit":
            pass

        if stage == "test":
            pass

    def train_dataloader(self):
        return

    def val_dataloader(self):
        return

    def test_dataloader(self):
        return