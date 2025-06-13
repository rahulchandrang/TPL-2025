class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class DataLoadingError(CustomError):
    """Raised when there is an error loading data"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class ModelTrainingError(CustomError):
    """Raised when there is an error during model training"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class PredictionError(CustomError):
    """Raised when there is an error during prediction"""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def retry_on_exception(func, retries=3):
    """Retries a function call if an exception occurs"""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt < retries - 1:
                continue
            else:
                raise e