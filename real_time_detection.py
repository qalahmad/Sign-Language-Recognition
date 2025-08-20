import cv2
import os
import numpy as np
from utils.mediapipe_utils import mediapipe_detection, draw_styled_landmarks, mp_holistic
from utils.data_utils import extract_keypoints 
import mediapipe as mp

# 1. new detection variables

# Holds the 30 frames
sequence = []
# Concatenate History of detections
sentence = []

predictions = []
# Confidence metric, only renders result if they are over threshold
threshold = 0.7

## TODO Probabliity visual

# Main loop
cap = cv2.VideoCapture(0)  # Try different indices if 0 doesn't work (e.g., 1, 2)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
                    
        # Read Feed from webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to read from camera")
            break

        # Make detections
        image, results = mediapipe_detection(frame, holistic)

        # Draw landmarks
        draw_styled_landmarks(image, results)
        
        # 2. Prediction Logic
        ## TODO Prediction logiv
        
        # 3. Viz Probabilities Side Bars
        ## TODO
                    
        # Show to screen
        cv2.imshow('OpenCV Feed', image)
                    
        # Break Gracefully
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows