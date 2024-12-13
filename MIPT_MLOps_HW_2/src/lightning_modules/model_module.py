import pytorch_lightning as pl
import torch
import torch.nn.functional as F
from torch import nn

class HadamardModel(pl.LightningModule):
    def __init__(self, cfg):
        super().__init__()
        self.save_hyperparameters()
        self.layer_1 = nn.Linear(cfg.input_dim, cfg.hidden_dim)
        self.layer_2 = nn.Linear(cfg.hidden_dim, cfg.output_dim)

    def forward(self, x):
        x = F.relu(self.layer_1(x))
        return self.layer_2(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.mse_loss(y_hat, y)
        self.log("train_loss", loss, on_step=True, on_epoch=True)
        return loss

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=self.hparams.learning_rate)