import os
import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd
import pytorch_lightning as pl

class HadamardDataset(Dataset):
    def __init__(self, dataset_path):
        if not os.path.exists(dataset_path):
            raise FileNotFoundError(f"Dataset path {dataset_path} does not exist.")
        self.data = pd.read_csv(dataset_path).values

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        x = self.data[idx, :-1]
        y = self.data[idx, -1]
        return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

class HadamardDataModule(pl.LightningDataModule):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg

    def setup(self, stage=None):
        self.dataset = HadamardDataset(self.cfg.dataset_path)

    def train_dataloader(self):
        return DataLoader(
            self.dataset,
            batch_size=self.cfg.batch_size,
            shuffle=self.cfg.shuffle,
            num_workers=self.cfg.num_workers
        )