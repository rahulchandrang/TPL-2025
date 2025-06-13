def deploy_model(model, deployment_config):
    """
    Deploys the trained model to a production environment.

    Parameters:
    model: The trained machine learning model to be deployed.
    deployment_config: Configuration settings for the deployment.

    Returns:
    str: Deployment status message.
    """
    # Implement the deployment logic here
    # This could involve using Azure ML SDK or Databricks API to deploy the model
    # For example:
    # from azureml.core import Model
    # Model.register(model_path=model_path, model_name=model_name, tags=tags, description=description)

    return "Model deployed successfully."