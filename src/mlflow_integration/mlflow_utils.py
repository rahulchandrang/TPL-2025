from mlflow import log_param, log_metric, start_run, end_run

def log_experiment_params(params):
    with start_run():
        for key, value in params.items():
            log_param(key, value)

def log_experiment_metrics(metrics):
    with start_run():
        for key, value in metrics.items():
            log_metric(key, value)

def log_model(model, model_name):
    import mlflow.sklearn
    mlflow.sklearn.log_model(model, model_name)