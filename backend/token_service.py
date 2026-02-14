import time
import hashlib

TOKEN_EXPIRY_SECONDS = 300  # 5 minutes

ACTIVE_TOKENS = {}


def issue_token(nonce):
    timestamp = str(time.time())
    raw = nonce + timestamp

    token = hashlib.sha256(raw.encode()).hexdigest()

    expiry = int(time.time()) + TOKEN_EXPIRY_SECONDS

    ACTIVE_TOKENS[token] = expiry

    return token


def validate_token(token):
    if token not in ACTIVE_TOKENS:
        return False

    if time.time() > ACTIVE_TOKENS[token]:
        del ACTIVE_TOKENS[token]
        return False

    return True
