import time

# Simple thresholds tuned for demo purposes
MIN_MOVEMENT_VARIANCE = 0.02
MIN_DURATION_SECONDS = 0.5


def compute_movement_variance(landmark_history):
    """
    landmark_history: list of numeric movement values over time
    Returns variance as a float
    """
    if len(landmark_history) < 2:
        return 0.0

    mean = sum(landmark_history) / len(landmark_history)
    variance = sum((x - mean) ** 2 for x in landmark_history) / len(landmark_history)
    return variance


def emotion_score(landmark_history, start_time):
    """
    Produces a human-likeness score based on:
    - smooth temporal change
    - non-zero micro movement
    """

    duration = time.time() - start_time
    if duration < MIN_DURATION_SECONDS:
        return 0.0

    variance = compute_movement_variance(landmark_history)

    if variance < MIN_MOVEMENT_VARIANCE:
        return 0.0

    # Normalize to [0,1] range for demo
    score = min(1.0, variance * 10)
    return score
