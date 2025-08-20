# 1-38 Written by Jayden Truong on 2025-02-04
import cv2
import os
import numpy as np
from utils.mediapipe_utils import mediapipe_detection, draw_styled_landmarks, mp_holistic
from utils.data_utils import extract_keypoints 
import mediapipe as mp
import sys

#DONE BY QUSAI
#TODO: From the tutorial Cell 4 Setup folders for data collection before the main loop
DATA_PATH = os.path.join('MP_Data') # path for exported data,  numpy arrays 
actions = np.array(['hello', 'thanks', 'iloveyou']) # Actions that we try to detect
no_sequences = 30 # 30 videos worth of data
sequence_length = 30 # videos are 30 frames long

# Create a resizable window for better visibility of text
cv2.namedWindow('OpenCV Feed', cv2.WINDOW_NORMAL)
cv2.resizeWindow('OpenCV Feed', 1280, 720)  # Set a larger default size

for action in actions: # Loop through each action
    for sequence in range(no_sequences): # Loop through each sequence (video)
        try:
            ## Makedirs just makes a new directory if it doesn't exist
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
try:
    with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
        ## Loop through actions, sequences, and frames from above
        for action in actions:
            for sequence in range(no_sequences):
                for frame_num in range(sequence_length):
                    
                    # Read Feed from webcam
                    ret, frame = cap.read()
                    if not ret:
                        print("Failed to read from camera")
                        break

                    # Make detections
                    image, results = mediapipe_detection(frame, holistic)

                    # Draw landmarks
                    draw_styled_landmarks(image, results)
                    
                    ## Taking a break between frames to make sure the model is not overloaded
                    ## Applying wait logic
                    if frame_num == 0:
                        cv2.putText(image, 'STARTING COLLECTION', (120, 200),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3, cv2.LINE_AA)
                        cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow('OpenCV Feed', image)
                        key = cv2.waitKey(2000)
                        if key & 0xFF == ord('q'):
                            raise KeyboardInterrupt
                    else:
                        cv2.putText(image, f'Collecting frames for {action} Video Number {sequence}', (15, 30),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                        cv2.putText(image, f'Frame: {frame_num}/{sequence_length}', (15, 60),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                        # Show to screen
                        cv2.imshow('OpenCV Feed', image)
                    
                    #Extract Keypoints
                    keypoints = extract_keypoints(results)
                    npy_path = os.path.join(DATA_PATH, action, str(sequence), str(frame_num))
                    np.save(npy_path, keypoints)
                    
                    #NOT FROM TUTORIAL
                    # Check for quit key at each frame
                    # Wasn't allowing me to quit during collection, so added this so you dont have to ctrl c in terminal, has same function though
                    
                    key = cv2.waitKey(10)
                    if key & 0xFF == ord('q'):
                        raise KeyboardInterrupt
                    elif key & 0xFF == ord('f'):  # Add fullscreen toggle with 'f' key
                        ## THIS IS NOT FROM TUTORIAL
                        ## Added a fullscreen mode for better compatibility with different screen sizes
                        if cv2.getWindowProperty('OpenCV Feed', cv2.WND_PROP_FULLSCREEN) == cv2.WINDOW_NORMAL:
                            cv2.setWindowProperty('OpenCV Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                        else:
                            cv2.setWindowProperty('OpenCV Feed', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

except KeyboardInterrupt:
    print("Data collection stopped by user")
finally:
    # Make sure we always release the camera
    cap.release()
    cv2.destroyAllWindows()
    print("Data collection completed or interrupted")