# Sign Language Recognition (Work in Progress)

This repository is an **active work in progress** focused on building a real-time sign language recognition system using computer vision and deep learning techniques.  
The long-term goal of this project is to **develop a transcription extension for video calling services**, enabling seamless accessibility by converting sign language into text during live conversations.  

While the current implementation is still in its early stages, progress is ongoing. This document outlines the present state of development and the roadmap toward full integration into video conferencing platforms.  

---

## Table of Contents
- [Project Overview](#project-overview)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Folder Structure](#folder-structure)  
- [Development Roadmap](#development-roadmap)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview
The project leverages **TensorFlow**, **MediaPipe**, and related libraries to detect, process, and classify hand gestures in real time.  
Initial work includes building and training LSTM models on collected data, testing webcam-based recognition, and iterating on detection accuracy.  

This forms the foundation for the broader objective: integrating sign language recognition into live **video calling platforms** (e.g., Zoom, Google Meet, Microsoft Teams) as a transcription extension.  

---

## Prerequisites
- Python **3.8+** (tested on **3.10.11** and **3.12.8**)  
- Webcam for real-time recognition  
- `pip` for package management  

---

## Installation
1. Clone the repository:  
   ```sh
   git clone https://ourrepo.git
   cd ourrepo
   ```
2. Create and activate a virtual environment:  
   ```sh
   python -m venv venv
   source venv/bin/activate    # macOS/Linux
   venv\Scripts\activate       # Windows
   ```
3. Install dependencies:  
   ```sh
   pip install -r requirements.txt
   ```

---

## Usage
1. Activate your virtual environment.  
2. Run the collection or detection scripts, for example:  
   ```sh
   python collect_data.py
   python detect.py
   ```  
3. Controls:  
   - Press **q** to close the webcam window.  
   - Use **Ctrl+C** in terminal to exit the process.  

---

## Folder Structure
```
sign_language_detection/
│── data/                 # Collected keypoint sequences
│── models/               # Trained LSTM models
│── utils/                # Helper functions
│   ├── mediapipe_utils.py
│   ├── data_utils.py
│   └── model_utils.py
│── collect_data.py        # Data collection script
│── train.py               # Model training script
│── detect.py              # Real-time detection script
│── test_webcam.py         # Webcam test script
│── requirements.txt       # Dependencies
```

---

## Development Roadmap
This project is under **active development**. The following milestones represent the path forward:

1. **Data Pipeline**  
   - Expand the dataset with diverse sign language gestures.  
   - Improve preprocessing for better feature extraction.  

2. **Model Improvements**  
   - Train advanced architectures (beyond LSTMs) for improved accuracy.  
   - Benchmark performance across multiple environments.  

3. **System Integration**  
   - Develop APIs to expose the recognition engine.  
   - Create a local extension capable of running during video calls.  

4. **Transcription Layer**  
   - Convert recognized gestures into text output in real time.  
   - Ensure compatibility with major video conferencing platforms.  

5. **Accessibility Focus**  
   - Optimize for latency and accuracy.  
   - Design a user-friendly interface for seamless deployment.  

---

## Contributing
Contributions are welcome, but please note that this is a **work in progress** and the codebase may evolve quickly.  
- Fork the repository  
- Create a feature branch  
- Submit a pull request with clear documentation of changes  

---

## License
This project is licensed under the **MIT License**.  
