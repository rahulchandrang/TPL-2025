import logging
import sys
import time
from functools import wraps

# --- Custom Exceptions ---
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

class CircuitBreakerOpenError(CustomError):
    """Raised when the circuit breaker is open"""
    pass

# --- Retry Decorator ---
def retry_on_exception(retries=3, delay=2, exceptions=(Exception,)):
    """Retries a function call if an exception occurs"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt < retries - 1:
                        time.sleep(delay)
                        continue
                    else:
                        raise
        return wrapper
    return decorator

# --- Circuit Breaker Pattern ---
class CircuitBreaker:
    def __init__(self, max_failures=3, reset_timeout=10):
        self.max_failures = max_failures
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN

    def call(self, func, *args, **kwargs):
        if self.state == "OPEN":
            if (time.time() - self.last_failure_time) > self.reset_timeout:
                self.state = "CLOSED"
                self.failure_count = 0
            else:
                raise CircuitBreakerOpenError("Circuit breaker is open. Try again later.")
        try:
            result = func(*args, **kwargs)
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            if self.failure_count >= self.max_failures:
                self.state = "OPEN"
                logging.error(f"Circuit breaker opened after {self.max_failures} failures.")
                raise CircuitBreakerOpenError("Circuit breaker is open due to repeated failures.") from e
            raise

# --- Global Exception Handler Example ---
def global_exception_handler(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        # Allow keyboard interrupts to exit gracefully
        return
    logging.critical("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

sys.excepthook = global_exception_handler