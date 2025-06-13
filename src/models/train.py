def train_model(config):
    """
    Function to orchestrate the model training process.
    
    Args:
        config (dict): Configuration settings for training.
    
    Returns:
        model: Trained model instance.
    """
    from src.data.data_loader import DataLoader
    from src.features.build_features import build_features
    from src.models.model import Model

    # Load data
    data_loader = DataLoader()
    raw_data = data_loader.load_raw_data(config['data']['raw_data_path'])
    processed_data = data_loader.load_processed_data(config['data']['processed_data_path'])

    # Build features
    features, labels = build_features(processed_data)

    # Initialize and train model
    model = Model(config['model'])
    model.train(features, labels)

    return model