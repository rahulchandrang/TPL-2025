import pytest
from src.evaluation.evaluate import evaluate_model

def test_evaluate_model():
    # Sample predictions and true values for testing
    predictions = [100, 200, 300]
    true_values = [110, 190, 310]

    # Call the evaluate_model function
    metrics = evaluate_model(predictions, true_values)

    # Check if the metrics are calculated correctly
    assert 'rmse' in metrics
    assert 'accuracy' in metrics
    assert metrics['rmse'] >= 0
    assert metrics['accuracy'] >= 0 and metrics['accuracy'] <= 1

    # Additional assertions can be added based on expected values
    expected_rmse = 10.0  # Replace with the expected RMSE value
    expected_accuracy = 0.9  # Replace with the expected accuracy value
    assert metrics['rmse'] == expected_rmse
    assert metrics['accuracy'] == expected_accuracy