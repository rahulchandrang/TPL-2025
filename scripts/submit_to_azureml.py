def submit_job():
    import azureml.core
    from azureml.core import Workspace, Experiment, ScriptRunConfig, Environment

    # Load the Azure ML workspace configuration
    ws = Workspace.from_config()

    # Define the experiment name
    experiment_name = 'my_experiment'
    experiment = Experiment(workspace=ws, name=experiment_name)

    # Define the environment
    env = Environment.get(workspace=ws, name='my_environment')

    # Define the script run configuration
    src = ScriptRunConfig(source_directory='src',
                          script='model_training.py',
                          environment=env)

    # Submit the experiment
    run = experiment.submit(config=src)
    run.wait_for_completion(show_output=True)

    return run