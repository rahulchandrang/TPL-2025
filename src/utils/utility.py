import time
import re
import hashlib
from functools import wraps

# --- Rate Limiter ---
def rate_limiter(max_calls, period=1.0):
    """
    Decorator to limit the number of function calls within a time period.
    """
    last_reset = [time.time()]
    calls = [0]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            if now - last_reset[0] > period:
                last_reset[0] = now
                calls[0] = 0
            if calls[0] >= max_calls:
                sleep_time = period - (now - last_reset[0])
                if sleep_time > 0:
                    time.sleep(sleep_time)
                last_reset[0] = time.time()
                calls[0] = 0
            calls[0] += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

# --- Validation Functions ---
def validate_email(email: str) -> bool:
    """
    Validates if the provided string is a valid email address.
    """
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

def validate_positive_number(value) -> bool:
    """
    Checks if the value is a positive number.
    """
    return isinstance(value, (int, float)) and value > 0

def validate_password_strength(password: str) -> bool:
    """
    Checks if the password meets basic strength requirements.
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# --- Security Functions ---
def hash_string(input_string: str) -> str:
    """
    Returns a SHA-256 hash of the input string.
    """
    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()

def mask_sensitive_data(data: str, num_visible=4) -> str:
    """
    Masks all but the last num_visible characters of a sensitive string.
    """
    if len(data) <= num_visible:
        return '*' * len(data)
    return '*' * (len(data) - num_visible) + data[-num_visible:]