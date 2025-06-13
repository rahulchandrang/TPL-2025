class DataLoader:
    def __init__(self, config):
        self.config = config

    def load_raw_data(self, file_path):
        import pandas as pd
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            from src.utils.error_handler import handle_error
            handle_error(e)

    def load_processed_data(self, file_path):
        import pandas as pd
        try:
            data = pd.read_csv(file_path)
            return data
        except Exception as e:
            from src.utils.error_handler import handle_error
            handle_error(e)