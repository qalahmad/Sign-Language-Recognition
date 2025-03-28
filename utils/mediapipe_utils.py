# 1-39 Written by Jayden Truong on 2025-02-05
import cv2
import mediapipe as mp

mp_holistic = mp.solutions.holistic # Holistic model (Make detections)
mp_drawing = mp.solutions.drawing_utils # Drawing utilities (Make drawings)

def mediapipe_detection(image, model):
    # COLOR CONVERSION of the image BGR to RGB
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Sets image as non-writeable
    image.flags.writeable = False 
    # Make the prediction
    results = model.process(image) 
    # Sets image as writeable
    image.flags.writeable = True  
    # RGB to BGR
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) 
    return image, results 

# Applies the landmark visualizations to the current image in place
# For the color and thickness can change to whatever we prefer
def draw_styled_landmarks(image, results):
    # Draw face connections
    mp_drawing.draw_landmarks(image, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS,
                              mp_drawing.DrawingSpec(color=(80,110,10), thickness=1, circle_radius=1), #Color the landmarks
                              mp_drawing.DrawingSpec(color=(80,256,121), thickness=1, circle_radius=1)) #Color the connections
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2))
    # Draw left hand connections
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(121,22,76), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(color=(121,44,250), thickness=2, circle_radius=2))
    # Draw right hand connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=4),
                              mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2))











