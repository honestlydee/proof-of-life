import time
import hashlib
import uuid


def current_timestamp():
    """Return current UNIX timestamp (int)."""
    return int(time.time())


def generate_nonce():
    """Generate a unique session nonce."""
    return str(uuid.uuid4())


def hash_data(data: str):
    """Return SHA256 hash of input string."""
    return hashlib.sha256(data.encode()).hexdigest()


def is_expired(expiry_timestamp: int):
    """Check whether a timestamp has expired."""
    return current_timestamp() > expiry_timestamp
