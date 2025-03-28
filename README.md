
# ✨ Sign Language Recognition
Real-time sign language recognition using computer vision and deep learning. (Eggplant Engineers)

---

## 📋 Table of Contents
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Usage](#-usage)
- [Folder Structure](#-folder-structure)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔧 Prerequisites
Ensure you have the following installed before running the program:

- Python **3.8+** (Tested on **3.10.11** and **3.12.8**)
- Webcam (for real-time recognition)
- `pip` (Python package manager)

---

## 📦 Dependencies
The following Python packages will be automatically installed:

| Package       | Description                         |
|--------------|---------------------------------|
| TensorFlow   | Machine learning framework     |
| OpenCV       | Computer vision library        |
| MediaPipe    | Hand tracking & pose estimation |
| scikit-learn | Machine learning utilities     |
| matplotlib   | Data visualization             |
| numpy        | Numerical computing            |

---

## 💻 Installation
1. **Clone the Repository**
   ```sh
   git clone https://ourrepo.git
   cd ourrepo
   ```
2. **Create & Activate Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```

---

## 🚀 Usage
1. **Activate Virtual Environment**
   ```sh
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
2. **Run the Program**
   ```sh
   python collect_data.py
   ```
3. **Controls**
   - Press **'q'** to quit the webcam window
   - Use **Ctrl+C** in the terminal to stop the program

**Note:** Ensure your **webcam is connected and accessible** before running the program.

---

## 📂 Folder Structure
```
sign_language_detection/
│── data/                # Collected keypoint sequences
│── models/              # Saved LSTM models
│── utils/               # Helper functions
│   ├── mediapipe_utils.py  # MediaPipe detection/rendering
│   ├── data_utils.py       # Keypoint extraction
│   └── model_utils.py      # LSTM model builder
│── collect_data.py       # Data collection script
│── train.py              # Model training script
│── detect.py             # Real-time detection script
│── test_webcam.py        # Webcam test script
│── requirements.txt      # Dependencies
```

---

## 👥 Contributing
We welcome contributions! Follow these steps to contribute:

1. **Fork the repository**
2. **Create a new branch**
   ```sh
   git checkout -b feature/amazing_feature
   ```
3. **Commit your changes**
   ```sh
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```sh
   git push origin feature/amazing_feature
   ```
5. **Open a Pull Request**

---

## 📜 License
This project is licensed under the **MIT License**.

---


