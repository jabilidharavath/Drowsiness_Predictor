# 🚨 Drowsiness Predictor (EAR-Based)

A real-time drowsiness detection system that monitors eye activity using facial landmarks and Eye Aspect Ratio (EAR).  
The system detects prolonged eye closure (not normal blinking) and triggers a single audio + visual alert.

---

## 📌 Overview

Drowsiness and fatigue are major causes of accidents and reduced productivity.  
This project implements a real-time computer vision–based solution that continuously monitors a person’s eyes through a webcam and accurately detects drowsiness.

The system is designed to:
- Ignore natural blinking
- Detect prolonged eye closure
- Alert the user immediately using sound and on-screen warning

---

## ✅ Key Features

- Real-time webcam monitoring
- Face & eye landmark detection using MediaPipe (Face Landmarker – Tasks API)
- Eye Aspect Ratio (EAR) calculation for both eyes
- Temporal filtering and hysteresis to avoid false alerts from blinking
- Debounced alert (single beep per drowsy event)
- Live display of EAR value and counter

---

## 🧠 How It Works

1. Captures live video from the webcam  
2. Detects facial landmarks  
3. Extracts eye landmarks  
4. Computes Eye Aspect Ratio (EAR)  
5. Applies temporal logic to distinguish blinking from drowsiness  
6. Displays warning text and plays a beep sound when drowsiness is detected  

---

## 📐 Eye Aspect Ratio (EAR)

EAR is calculated using distances between eye landmarks:

EAR = (Vertical Distance 1 + Vertical Distance 2) / (2 × Horizontal Distance)

- Eyes open → EAR is higher  
- Eyes closed → EAR decreases  

---

## 🛠️ Technologies Used

- Python  
- OpenCV  
- MediaPipe (Tasks API)  
- winsound (Windows audio alert)

---

## 📂 Project Structure

Drowsiness-Predictor/
│
├── main.py
├── face_landmarker.task
└── README.md

---

## ▶️ How to Run

1. Clone the repository  
   git clone https://github.com/Bhukyasandhya/Drowsiness-Predictor.git  
   cd Drowsiness-Predictor  

2. Install dependencies  
   python -m pip install opencv-python mediapipe  

3. Run the application  
   python main.py  

4. Press **q** to exit

---

## 🔊 Alert Behavior

- Normal blinking → No alert  
- Prolonged eye closure (~1 second) →  
  - “DROWSINESS ALERT!” displayed on screen  
  - One beep sound  
- Alert resets only after eyes reopen  

---

## 🚀 Applications

- Driver monitoring systems  
- Workplace and night-shift safety  
- Student fatigue detection  
- Human behavior analysis  

---

## 🔮 Future Enhancements

- Yawn detection  
- Head pose / nod detection  
- Adaptive user-specific thresholds  
- Cross-platform audio alerts  

---

## 👤 Author

Sandhya

---

## ⭐ Final Note

This project demonstrates real-time computer vision, signal filtering, and human behavior modeling, making it suitable for interviews, academic evaluation, and practical demonstrations.
