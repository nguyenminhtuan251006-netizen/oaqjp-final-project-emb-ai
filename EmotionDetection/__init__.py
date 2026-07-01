"""Package initializer for the EmotionDetection application module.

This file imports the emotion_detector function from the
emotion_detection module so it can be used by the application.
"""

from .emotion_detection import emotion_detector

__all__ = ["emotion_detector"]
