# 1-38 Written by Jayden Truong on 2025-02-04
import cv2
import os
import numpy as np
from utils.mediapipe_utils import mediapipe_detection, draw_styled_landmarks, mp_holistic
from utils.data_utils import extract_keypoints 
import mediapipe as mp

#DONE BY QUSAI
#TODO: From the turotial Cell 4 Setup folders for data collection before the main loop
DATA_PATH = os.path.join('MP_Data') # path for exported data
actions = np.array(['hello', 'thanks', 'iloveyou']) # Actions that we try to detect
no_sequences = 30 # 30 videos worth of data
sequence_length = 30 # videos are 30 frames long

for action in actions: # Loop through each action
    for sequence in range(no_sequences): # Loop through each sequence (video)
        try:
            os.makedirs(os.path.join(DATA_PATH, action, str(sequence)))
        except:
            pass



# Main loop
cap = cv2.VideoCapture(0)  # Try different indices if 0 doesn't work (e.g., 1, 2)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set mediapipe model (Can change values to improve detection)
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
# while loop to keep the webcam open
    while cap.isOpened():
        # Read Feed from webcam
        ret, frame = cap.read()

        # Make detections
        image, results = mediapipe_detection(frame, holistic)

        # Draw landmarks
        draw_styled_landmarks(image, results)

        #Extract Keypoints
        keypoints = extract_keypoints(results)

        # Show to screen
        cv2.imshow('OpenCV Feed', image)

        # if the user presses the q key, the webcam will close       
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows() 