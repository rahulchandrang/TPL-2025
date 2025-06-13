class DataLoader:
    def __init__(self, raw_data_path, processed_data_path):
        self.raw_data_path = raw_data_path
        self.processed_data_path = processed_data_path

    def load_raw_data(self):
        import pandas as pd
        return pd.read_csv(self.raw_data_path)

    def load_processed_data(self):
        import pandas as pd
        return pd.read_csv(self.processed_data_path)