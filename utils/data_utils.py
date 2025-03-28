# DONE BY QUSAI
# #TODO: Extract keypoints From tutorial Cell 3 mainly

import numpy as np



def extract_keypoints(results):
    pose = []

    for res in results.pose_landmarks.landmark:
        test = np.array([res.x, res.y, res.z, res.visibility])
        pose.append(test)


    pose = np.array([res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark).flatten() if results.pose_landmarks else np.zeros(33 * 4) # or 132
    face = np.array([res.x, res.y, res.z] for res in results.face_landmarks.landmark).flatten() if results.face_landmarks else np.zeros(468 * 3) # or add 1404
    lh = np.array([res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark).flatten() if results.left_hand_landmarks else np.zeros(21 * 3)
    rh = np.array([res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark).flatten() if results.right_hand_landmarks else np.zeros(21 * 3)
    return np.concatenate([pose, face, lh, rh]) # concatenate all the keypoints into one array

   






   #The function below is better formated so you can uncomment it and comment the one above
   #but face landmarks are not included in this function so you have to add it. You can stick with the above function as well


# def extract_keypoints(results):
#     """
#     Extracts keypoints from Mediapipe results and returns a flattened numpy array.
    
#     Parameters:
#     results (object): Mediapipe holistic model results.
    
#     Returns:
#     np.ndarray: Flattened array containing pose, left-hand, and right-hand keypoints.
#     """

#     # Extract pose landmarks if available, else return zeros
#     if results.pose_landmarks:
#         pose = np.array([[res.x, res.y, res.z, res.visibility] 
#                          for res in results.pose_landmarks.landmark]).flatten()
#     else:
#         pose = np.zeros(33 * 4)  # 33 pose landmarks, each with 4 attributes

#     # Extract left hand landmarks if available, else return zeros
#     if results.left_hand_landmarks:
#         lh = np.array([[res.x, res.y, res.z] 
#                        for res in results.left_hand_landmarks.landmark]).flatten()
#     else:
#         lh = np.zeros(21 * 3)  # 21 landmarks, each with 3 attributes

#     # Extract right hand landmarks if available, else return zeros
#     if results.right_hand_landmarks:
#         rh = np.array([[res.x, res.y, res.z] 
#                        for res in results.right_hand_landmarks.landmark]).flatten()
       
#     else:
#         rh = np.zeros(21 * 3)

#     return np.concatenate([pose, lh, rh])

