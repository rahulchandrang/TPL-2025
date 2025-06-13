import os
import pandas as pd


class DataLoader:
    """
    Utility class for loading raw data files from the data/raw directory.
    """

    RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "raw")

    @staticmethod
    def load_csv(filename):
        """
        Loads a CSV file from the data/raw directory.
        """
        file_path = os.path.join(DataLoader.RAW_DATA_DIR, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"{file_path} does not exist.")
        return pd.read_csv(file_path)

    @staticmethod
    def list_raw_files():
        """
        Lists all files in the data/raw directory.
        """
        return os.listdir(DataLoader.RAW_DATA_DIR)