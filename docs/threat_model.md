# Threat Model

## Attacks Mitigated
- Replay attacks using recorded video or images
- Static deepfake impersonation
- Pre-generated AI video responses
- Token reuse beyond validity window

## Techniques Used
- Randomized, time-bound visual challenges
- Real-time liveness and motion verification
- Temporal emotion and expression transition analysis
- Short-lived Proof-of-Life access tokens

## Known Limitations
- Does not defend against advanced real-time AI puppeteering
- Relies on camera availability and lighting conditions
- Demo implementation uses simplified CV thresholds

## Design Philosophy
The system focuses on layered, practical defenses that significantly raise the cost of impersonation while remaining deployable and explainable within real-world constraints.
