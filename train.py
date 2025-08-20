import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import mediapipe as mp
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import TensorBoard

# Define the same constants as in collect_data.py
# Necessary instead of importing them from collect_data.py
# because we want to keep the code modular and avoid circular imports
DATA_PATH = os.path.join('MP_Data')
actions = np.array(['hello', 'thanks', 'iloveyou'])
no_sequences = 30
sequence_length = 30

#TODO: Cell 6 from tutorial Preprocess Data and Create Labels

# Map actions to numbers
# This is necessary for the LSTM model to understand the labels
label_map = {label:num for num, label in enumerate(actions)}

# read in all our data and convert it to numpy arrays
sequences, labels = [], []
for action in actions:
    for sequence in range(no_sequences):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), f"{frame_num}.npy"))
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

# Convert to numpy arrays
# This is necessary for the LSTM model to understand the data
x = np.array(sequences)
y = to_categorical(labels).astype(int)

# Setup train and test partition
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05)



#TODO: From Cell 7 Build and Train LSTM Model

# Web app that monitors the training process (Makes logs)
log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)

# Neural network model 6 layers
model = Sequential() # Sequential API
# If you are going to layer you must return sequences to the next layer !!
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 1662))) # 1662 is the number of features
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax')) # 3 actions

# Metrics is optional but gives a better idea of how the model is doing
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.fit(x_train, y_train, epochs=200, callbacks=[tb_callback])

model.save('action.h5')
print('Model Saved')

