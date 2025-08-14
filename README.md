# Head Tracking with Eye Blink Detection

A **Python-based hands-free mouse control system** that uses **computer vision** to track head movements and detect eye blinks, allowing complete mouse control without using your hands. Designed for **accessibility**, **assistive technology**, and **hands-free computing**.

---

## ✨ Features

### 🎯 Head Movement Tracking
- **Real-time head tracking** using [MediaPipe Face Mesh](https://developers.google.com/mediapipe/solutions/vision/face_mesh)
- **Smooth cursor movement** with configurable sensitivity
- **3D head orientation** detection: yaw, pitch, and roll
- **Calibration system** for personalized setup
- **Smoothing filters** to reduce jittery movement

### 👁 Eye Blink Detection
- **EAR (Eye Aspect Ratio)** calculation for accurate blink detection
- **Automatic mouse clicking** when blinks are detected
- **Configurable sensitivity** and cooldown period
- **Visual feedback** with real-time EAR display
- **Toggle controls** for enabling/disabling blink detection

---

## 🚀 Quick Start

### Prerequisites
- Python **3.7 or higher**
- A working **webcam**
- Good, consistent **lighting conditions**

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mahamudul-hasan-cse/head-tracking-blink-detection.git
   cd head-tracking-blink-detection
2. Install dependencies
pip install -r requirements.txt
3. Run the main application
python MonitorTracking.py

⚙️ Configuration
Head Tracking Sensitivity
yawDegrees = 20    # Degrees left/right to reach screen edges
pitchDegrees = 10  # Degrees up/down to reach screen edges

Blink Detection Settings
EYE_AR_THRESH = 0.21          # Blink sensitivity
EYE_AR_CONSEC_FRAMES = 2      # Frames eyes must be closed to trigger click
blink_cooldown = 0.5          # Seconds between clicks
📸 Screenshots
Here are
F7: Toggle mouse control
F8: Toggle blink Detection
C: Calibrate
Q: Quit
<img width="1287" height="512" alt="Screenshot_3" src="https://github.com/user-attachments/assets/405b889c-a5da-4e22-a2e3-be7d3bd081e6" />
📁 Project Structure
head-tracking-blink-detection/
├── MonitorTracking.py           # Main application
├── test_blink_detection.py      # Blink detection test
├── CursorCircle.py               # Visual cursor overlay
├── test_camera.py                # Camera test utility
├── run_head_tracking.bat         # Batch file runner
├── run_head_tracking.ps1         # PowerShell runner
├── run_head_tracking_improved.bat# Improved batch file runner
├── stop_head_tracking.bat        # Stop script
├── run_project.py                 # Alternative Python runner
├── run_project_improved.py        # Improved Python runner
├── BLINK_DETECTION_README.md     # Detailed blink detection guide
├── requirements.txt              # Python dependencies
├── README.md                     # Main documentation
├── LICENSE                       # MIT License
└── .gitignore                    # Ignore unnecessary files

🔧 Troubleshooting
Common Issues

Head tracking not working → Check lighting, camera permissions, and make sure webcam is detected.

Blink detection too sensitive → Increase EYE_AR_THRESH (e.g., 0.25).

Blink detection not sensitive enough → Decrease EYE_AR_THRESH (e.g., 0.18).

Cursor movement too fast/slow → Adjust yawDegrees and pitchDegrees.

Camera feed lagging → Close background apps using the camera.

📊 Technical Details
Eye Aspect Ratio (EAR)

Uses 6 facial landmarks around each eye for blink detection.

Compares vertical eye distance with horizontal eye distance.

Head Tracking Algorithm

Face Mesh detection with MediaPipe

Extract 3D facial landmark coordinates

Map yaw/pitch to screen coordinates

Apply smoothing filters

Control mouse cursor with PyAutoGUI

🛠 Dependencies

opencv-python — video capture and image processing

mediapipe — head and facial landmark detection

numpy — numerical calculations

pyautogui — mouse control

keyboard — hotkey detection

Install all with:

pip install -r requirements.txt

Real-time head tracking using MediaPipe Face Mesh

🤝 Contributing

Fork the repository

Create a new branch:

git checkout -b feature-name


Commit your changes:

git commit -m "Add new feature"


Push to your fork and create a Pull Request

📝 License

This project is licensed under the MIT License — see the LICENSE file for details.

⚠️ Safety Notes

Take regular breaks to avoid eye strain.

Use in well-lit environments.

Not recommended for prolonged usage without breaks.


---
