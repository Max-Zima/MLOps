import pytest
from ..src.lightning_modules.data_module import HadamardDataModule

def test_data_module():
    cfg = {
        "dataset_path": "data/processed_data.csv",
        "batch_size": 32,
        "shuffle": True,
        "num_workers": 4
    }
    data_module = HadamardDataModule(cfg)
    data_module.setup()
    assert len(data_module.dataset) > 0