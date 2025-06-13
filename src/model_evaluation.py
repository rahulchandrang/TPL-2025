def evaluate_model(model, test_data):
    """
    Evaluate the trained model using the test data and return evaluation metrics.
    
    Parameters:
    model: The trained machine learning model to evaluate.
    test_data: The data to use for evaluation, typically a DataFrame containing features and labels.
    
    Returns:
    metrics: A dictionary containing evaluation metrics such as accuracy, precision, recall, etc.
    """
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

    # Separate features and labels
    X_test = test_data.drop('label', axis=1)
    y_test = test_data['label']

    # Make predictions
    predictions = model.predict(X_test)

    # Calculate metrics
    metrics = {
        'accuracy': accuracy_score(y_test, predictions),
        'precision': precision_score(y_test, predictions, average='weighted'),
        'recall': recall_score(y_test, predictions, average='weighted'),
        'f1_score': f1_score(y_test, predictions, average='weighted')
    }

    return metrics