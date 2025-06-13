def run_pipeline():
    import os
    from src.data.data_loader import DataLoader
    from src.features.feature_engineering import FeatureEngineer
    from src.models.model import PricingModel
    from src.utils.logger import Logger
    from src.utils.error_handler import CustomError
    from src.mlflow_integration.mlflow_utils import log_experiment

    # Setup logging
    logger = Logger()
    logger.setup_logging()

    try:
        # Load raw data
        data_loader = DataLoader()
        raw_data = data_loader.load_raw_data()
        logger.log_message("Raw data loaded successfully.")

        # Feature engineering
        feature_engineer = FeatureEngineer()
        features = feature_engineer.create_features(raw_data)
        logger.log_message("Features created successfully.")

        # Train the model
        pricing_model = PricingModel()
        pricing_model.train(features)
        logger.log_message("Model trained successfully.")

        # Log experiment to MLflow
        log_experiment(pricing_model)
        logger.log_message("Experiment logged to MLflow.")

    except CustomError as e:
        logger.log_message(f"An error occurred: {str(e)}")
    except Exception as e:
        logger.log_message(f"An unexpected error occurred: {str(e)}")