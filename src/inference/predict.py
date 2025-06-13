def make_prediction(model_path, input_data):
    import joblib
    import pandas as pd

    # Load the trained model
    model = joblib.load(model_path)

    # Prepare the input data
    input_df = pd.DataFrame(input_data)

    # Make predictions
    predictions = model.predict(input_df)

    return predictions