import torch
from src.lightning_modules.model_module import HadamardModel

def test_model_forward():
    cfg = {
        "input_dim": 3,
        "hidden_dim": 64,
        "output_dim": 3,
        "learning_rate": 0.001
    }
    model = HadamardModel(cfg)
    x = torch.rand(1, 3)
    y = model(x)
    assert y.shape == (1, 3)