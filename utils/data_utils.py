# DONE BY QUSAI
# #TODO: Extract keypoints From tutorial Cell 3 mainly

import numpy as np

def extract_keypoints(results):
    """
    Extracts keypoints from Mediapipe results and returns a flattened numpy array.
    
    Parameters:
    results (object): Mediapipe holistic model results.
    
    Returns:
    np.ndarray: Flattened array containing pose, face, left-hand, and right-hand keypoints.
    """
    # Extract pose landmarks if available, else return zeros
    pose = np.array([[res.x, res.y, res.z, res.visibility] 
                     for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33 * 4)

    # Extract face landmarks if available, else return zeros
    face = np.array([[res.x, res.y, res.z] 
                     for res in results.face_landmarks.landmark]).flatten() if results.face_landmarks else np.zeros(468 * 3)

    # Extract left hand landmarks if available, else return zeros
    lh = np.array([[res.x, res.y, res.z] 
                   for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)

    # Extract right hand landmarks if available, else return zeros
    rh = np.array([[res.x, res.y, res.z] 
                   for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21 * 3)

    # Concatenate all the keypoints into one array
    return np.concatenate([pose, face, lh, rh])

