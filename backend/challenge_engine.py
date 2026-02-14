import random
import time
import uuid

CHALLENGE_POOL = [
    ["turn_head_left", "blink"],
    ["smile", "neutral"],
    ["open_mouth", "nod"],
    ["blink", "smile"],
]

CHALLENGE_EXPIRY_SECONDS = 15


def generate_challenge():
    challenge = random.choice(CHALLENGE_POOL)
    nonce = str(uuid.uuid4())
    expiry = int(time.time()) + CHALLENGE_EXPIRY_SECONDS

    return {
        "challenge": challenge,
        "nonce": nonce,
        "expires_at": expiry
    }
