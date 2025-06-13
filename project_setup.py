import os
import json
import logging
import logging.config
from logging import Logger
from pythonjsonlogger import jsonlogger
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import time
import re
from functools import wraps

# --- Project Structure Creation ---
PROJECT_STRUCTURE = [
    "data/raw",
    "data/processed",
    "data/external",
    "notebooks",
    "src/data",
    "src/features",
    "src/models",
    "src/pipelines",
    "src/utils",
    "src/mlflow_integration",
    "tests"
]

def create_project_structure(base_path="."):
    for folder in PROJECT_STRUCTURE:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)
    print("Project structure created.")

# --- Structured Logging with JSON & Azure App Insights ---
class AppInsightsHandler(logging.Handler):
    def emit(self, record):
        # Placeholder for Azure Application Insights integration
        # In production, use Azure Monitor OpenCensus/Opentelemetry exporters
        log_entry = self.format(record)
        # Send log_entry to Azure Application Insights here
        pass

def setup_logging():
    logger = logging.getLogger("ml_project")
    logger.setLevel(logging.INFO)
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter('%(asctime)s %(levelname)s %(name)s %(message)s')
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    # Add Azure App Insights handler (stub)
    logger.addHandler(AppInsightsHandler())
    return logger

logger = setup_logging()

# --- Error Handling Utilities ---
class MLProjectException(Exception):
    """Base exception for ML project errors."""

class RetryException(MLProjectException):
    """Exception for retryable errors."""

def retry(max_attempts=3, delay=2, exceptions=(Exception,)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempts += 1
                    logger.warning({"msg": f"Retry {attempts}/{max_attempts} after error: {e}"})
                    if attempts == max_attempts:
                        logger.error({"msg": "Max retries reached.", "error": str(e)})
                        raise RetryException(f"Function {func.__name__} failed after {max_attempts} attempts") from e
                    time.sleep(delay)
        return wrapper
    return decorator

# --- Azure Key Vault Integration ---
class AzureKeyVaultManager:
    def __init__(self, vault_url: str):
        self.vault_url = vault_url
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=self.vault_url, credential=self.credential)

    @retry(max_attempts=3, delay=1, exceptions=(Exception,))
    def get_secret(self, secret_name: str) -> str:
        secret = self.client.get_secret(secret_name)
        logger.info({"msg": f"Fetched secret: {secret_name}"})
        return secret.value

# --- Utility Functions ---
def rate_limiter(max_calls, period=1.0):
    """Simple rate limiter decorator."""
    def decorator(func):
        last_reset = [time.time()]
        calls = [0]
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_reset[0] > period:
                last_reset[0] = now
                calls[0] = 0
            if calls[0] >= max_calls:
                logger.warning({"msg": "Rate limit exceeded, sleeping..."})
                time.sleep(period - (now - last_reset[0]))
                last_reset[0] = time.time()
                calls[0] = 0
            calls[0] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_email(email: str) -> bool:
    """Simple email validator."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    valid = re.match(pattern, email) is not None
    logger.info({"msg": f"Email validation for {email}: {valid}"})
    return valid

def validate_positive_number(value) -> bool:
    """Check if value is a positive number."""
    valid = isinstance(value, (int, float)) and value > 0
    logger.info({"msg": f"Positive number validation for {value}: {valid}"})
    return valid

# --- Example Usage ---
if __name__ == "__main__":
    create_project_structure()
    # Example: Using Key Vault (replace with your vault URL and secret name)
    # vault_url = "https://<your-key-vault-name>.vault.azure.net/"
    # kv_manager = AzureKeyVaultManager(vault_url)
    # secret = kv_manager.get_secret("MY_SECRET")
    # logger.info({"msg": f"Secret value: {secret}"})
    # Example: Using rate limiter and validators
    @rate_limiter(max_calls=2, period=5)
    def test_func():
        logger.info({"msg": "Function called"})
    test_func()
    test_func()
    print(validate_email("test@example.com"))
    print(validate_positive_number(42))