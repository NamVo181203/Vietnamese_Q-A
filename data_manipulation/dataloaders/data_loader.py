from torch.utils.data import DataLoader, Dataset
from datasets import Dataset as HFDataset


class MyDataset(Dataset):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.dataset = self._create_hf_dataset()
        self.dataset = self.dataset.map(self._process_hf_dataset)

    def _create_hf_dataset(self):
        # read dataset from json file
        # path to json file included in yaml configs
        dataset = HFDataset.from_json(self.path)
        return dataset

    def _process_hf_dataset(self, batch):
        # process audio by bind the audio_dir
        # with an audio_path process the label
        # by mapping the phonemes with label
        # in defined vocab
        return batch

    def __len__(self):
        # Return length of dataset
        return len(self.dataset)

    def __getitem__(self, idx):
        # Return each element in a dataset with an index
        return 0


class MyDataloader(DataLoader):
    def __init__(self):
        super().__init__()

    def collate_function(self, batch):
        return batch