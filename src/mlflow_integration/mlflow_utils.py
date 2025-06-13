import mlflow
from mlflow import log_param, log_metric, start_run, end_run

def setup_mlflow_tracking(uri: str = None, experiment_name: str = None):
    """
    Sets up MLflow tracking URI and experiment name.
    """
    if uri:
        mlflow.set_tracking_uri(uri)
    if experiment_name:
        mlflow.set_experiment(experiment_name)

def log_experiment_params(params):
    """
    Logs experiment parameters to MLflow.
    """
    for key, value in params.items():
        log_param(key, value)

def log_experiment_metrics(metrics):
    """
    Logs experiment metrics to MLflow.
    """
    for key, value in metrics.items():
        log_metric(key, value)

def log_model(model, model_name):
    """
    Logs a trained model to MLflow.
    """
    import mlflow.sklearn
    mlflow.sklearn.log_model(model, model_name)

def run_mlflow_experiment(params, metrics, model, model_name, uri=None, experiment_name=None):
    """
    Complete MLflow experiment run: setup, log params, metrics, and model.
    """
    setup_mlflow_tracking(uri, experiment_name)
    with start_run():
        log_experiment_params(params)
        log_experiment_metrics(metrics)
        log_model(model, model_name)
        end_run()