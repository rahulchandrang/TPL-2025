# GlobalMart Tide Dynamic Pricing Project

## Overview
This project implements a dynamic pricing model for Tide products at GlobalMart. The model leverages historical sales data, market trends, and customer behavior to optimize pricing strategies, aiming to maximize revenue while remaining competitive in the market.

## Project Structure
The project follows a standardized machine learning project structure, which includes the following directories and files:

- **config/**: Contains configuration files for the project.
  - `config.yaml`: Model parameters and environment settings.
  - `logging.yaml`: Logging configuration.

- **credentials/**: Contains secure credential management files.
  - `.env.example`: Template for environment variables.

- **data/**: Directory for storing datasets.
  - `raw/`: Raw data files.
  - `processed/`: Processed data files.
  - `external/`: External data sources.

- **notebooks/**: Jupyter notebooks for exploratory data analysis.
  - `exploratory_analysis.ipynb`: Contains visualizations and insights.

- **src/**: Source code for the project.
  - `data/`: Data loading utilities.
    - `data_loader.py`: Class for loading datasets.
  - `features/`: Feature engineering utilities.
    - `feature_engineering.py`: Class for feature extraction and transformation.
  - `models/`: Machine learning models.
    - `model.py`: Class for training and predicting with the pricing model.
  - `pipelines/`: Data processing and model training pipelines.
    - `train_pipeline.py`: Orchestrates the training process.
  - `utils/`: Utility functions and classes.
    - `logger.py`: Structured logging utilities.
    - `error_handler.py`: Error handling mechanisms.
    - `credentials_manager.py`: Secure credential management.
  - `mlflow_integration/`: Integration with MLflow for experiment tracking.
    - `mlflow_utils.py`: Functions for logging experiments and metrics.

- **tests/**: Unit tests for the project.
  - `test_model.py`: Tests for the PricingModel class.

- **requirements.txt**: Lists the dependencies required for the project.

- **.gitignore**: Specifies files and directories to be ignored by Git.

- **MLproject**: Defines the project for MLflow, specifying entry points and parameters.

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/globalmart-tide-dynamic-pricing.git
   cd globalmart-tide-dynamic-pricing
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env` and fill in the required credentials.

5. Run the exploratory analysis notebook to understand the data:
   - Open `notebooks/exploratory_analysis.ipynb` in Jupyter Notebook.

6. Train the dynamic pricing model:
   - Execute the training pipeline by running `src/pipelines/train_pipeline.py`.

## Usage
- Use the `PricingModel` class in `src/models/model.py` to train and make predictions.
- Utilize MLflow for tracking experiments and metrics.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for discussion.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

### Logging and Monitoring

- The project uses structured JSON logging for all modules, configured via `config/logging.yaml`.
- Logs can be integrated with Azure Application Insights for production monitoring (see `src/utils/logger.py`).

### Error Handling

- Custom exceptions, retry decorators, and a circuit breaker pattern are implemented in `src/utils/error_handler.py`.
- A global exception handler ensures all uncaught exceptions are logged.

### Secure Configuration Management

- Secrets and sensitive configuration are managed using Azure Key Vault via `src/utils/credentials_manager.py`.
- Environment variables can be loaded from `.env` files or directly from Key Vault.

### Utility Modules

- Common utilities such as rate limiting, data validation, and security helpers are provided in `src/utils/utility.py`.

### MLflow Experiment Tracking

- MLflow is used for experiment tracking and model management.
- Configuration and logging utilities are in `src/mlflow_integration/mlflow_utils.py`.
- The `MLproject` file defines MLflow entry points for training and serving.

### CI/CD

- Automated testing and deployment are configured via GitHub Actions in `.github/workflows/ci-cd.yml`.

### Project Initialization

- Use `project_setup.py` to automatically create the project folder structure and demonstrate logging, error handling, and utility usage.