import unittest
from src.data.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.data_loader = DataLoader()

    def test_load_raw_data(self):
        raw_data = self.data_loader.load_raw_data()
        self.assertIsNotNone(raw_data)
        self.assertGreater(len(raw_data), 0)

    def test_load_processed_data(self):
        processed_data = self.data_loader.load_processed_data()
        self.assertIsNotNone(processed_data)
        self.assertGreater(len(processed_data), 0)

if __name__ == '__main__':
    unittest.main()