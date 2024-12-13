import hydra
from omegaconf import DictConfig
import pytorch_lightning as pl
from ..src.lightning_modules.data_module import HadamardDataModule
from ..src.lightning_modules.model_module import HadamardModel

@hydra.main(config_path="../configs", config_name="config")
def train(cfg: DictConfig):
    pl.seed_everything(cfg.trainer.seed)
    data_module = HadamardDataModule(cfg.data)
    model = HadamardModel(cfg.model)

    trainer = pl.Trainer(**cfg.trainer)
    trainer.fit(model, datamodule=data_module)

if __name__ == "__main__":
    train()