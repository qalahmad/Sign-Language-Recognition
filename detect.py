import numpy as np
import os
from tensorflow.keras.models import load_model
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score

# Define the same constants as in collect_data.py
# Necessary instead of importing them from collect_data.py
# because we want to keep the code modular and avoid circular imports
DATA_PATH = os.path.join('MP_Data')
actions = np.array(['hello', 'thanks', 'iloveyou'])
no_sequences = 30
sequence_length = 30

# Load the model
try:
    model = load_model('action.h5')
    print("Model loaded successfully!")
except:
    print("Error: Could not load model 'action.h5'")
    exit()

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

# Make Predictions
print("\nMaking predictions on test data...")
yhat = model.predict(x_train)

# Take the predictions and convert them to class indices
ytrue = np.argmax(y_train, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()

# Calculate confusion matrix
print("\nConfusion Matrix:")
conf_matrix = multilabel_confusion_matrix(ytrue, yhat)
print(conf_matrix)

# Calculate accuracy
acc = accuracy_score(ytrue, yhat)
print(f"\nAccuracy: {acc*100:.2f}%")