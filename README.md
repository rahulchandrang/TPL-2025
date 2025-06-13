# Azure ML and Databricks Machine Learning Project

This project is designed to facilitate machine learning workflows using Azure Databricks and Azure Machine Learning. It includes a structured approach to data handling, model training, evaluation, and deployment.

## Project Structure

```
azure-ml-databricks-ml-project
├── data
│   ├── raw
│   └── processed
├── notebooks
│   └── example_notebook.py
├── src
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── utils.py
├── configs
│   ├── databricks_config.json
│   └── azureml_config.json
├── scripts
│   ├── submit_to_azureml.py
│   └── deploy_model.py
├── .github
│   └── workflows
│       └── ci-cd.yml
├── requirements.txt
├── environment.yml
├── .gitignore
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd azure-ml-databricks-ml-project
   ```

2. **Install Dependencies**
   You can install the required Python packages using either `pip` or `conda`.

   Using pip:
   ```bash
   pip install -r requirements.txt
   ```

   Using conda:
   ```bash
   conda env create -f environment.yml
   conda activate <environment-name>
   ```

3. **Configure Azure Services**
   Update the configuration files in the `configs` directory with your Azure Databricks and Azure Machine Learning settings.

4. **Data Preparation**
   Place your raw data files in the `data/raw` directory. Use the scripts in the `src` directory to preprocess the data.

5. **Model Training**
   Use the `src/model_training.py` script to train your machine learning models.

6. **Model Evaluation**
   Evaluate your trained models using the functions provided in `src/model_evaluation.py`.

7. **Deployment**
   Deploy your model using the `scripts/deploy_model.py` script.

## CI/CD Integration

This project includes a GitHub Actions workflow defined in `.github/workflows/ci-cd.yml` for continuous integration and deployment. Ensure that your GitHub repository is set up to trigger this workflow on push events.

## Usage Guidelines

Refer to the individual scripts and notebooks for detailed usage instructions and examples. The `notebooks/example_notebook.py` provides a practical example of how to use the functions defined in the `src` directory.

## License

This project is licensed under the MIT License - see the LICENSE file for details.