from src.data.data_loader import DataLoader
from src.features.feature_engineering import create_features
from src.models.model import DynamicPricingModel
import pandas as pd
import yaml

def load_config(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def main():
    # Load configuration
    config = load_config('src/config/config.yaml')
    
    # Initialize DataLoader
    data_loader = DataLoader(config['data']['raw_data_path'], config['data']['processed_data_path'])
    
    # Load processed data
    processed_data = data_loader.load_processed_data()
    
    # Create features
    features = create_features(processed_data)
    
    # Initialize and train the model
    model = DynamicPricingModel()
    model.train(features)

if __name__ == "__main__":
    main()