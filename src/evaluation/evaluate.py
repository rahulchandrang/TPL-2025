def evaluate_model(predictions, true_values):
    from sklearn.metrics import mean_squared_error, accuracy_score
    import numpy as np

    rmse = np.sqrt(mean_squared_error(true_values, predictions))
    accuracy = accuracy_score(true_values, np.round(predictions))

    return {
        'RMSE': rmse,
        'Accuracy': accuracy
    }