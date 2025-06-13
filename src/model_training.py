class ModelTrainer:
    def __init__(self, model, data):
        self.model = model
        self.data = data

    def train_model(self):
        X_train, y_train = self.data
        self.model.fit(X_train, y_train)
        return self.model

    def save_model(self, filepath):
        import joblib
        joblib.dump(self.model, filepath)