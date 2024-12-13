import os
import pandas as pd

def preprocess(raw_data_path, processed_data_path):
    if not os.path.exists(raw_data_path):
        raise FileNotFoundError(f"Raw data path {raw_data_path} does not exist.")

    raw_data = pd.read_csv(raw_data_path)
    processed_data = raw_data.dropna()  # Удаление пропусков
    processed_data.to_csv(processed_data_path, index=False)

if __name__ == "__main__":
    preprocess("data/raw_data.csv", "data/processed_data.csv")