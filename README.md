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
- Python **3.7 or higher(used 3.11.9)**
- A working **webcam**
- Good, consistent **lighting conditions**

### Installation

1. **Clone the repository**
   git clone https://github.com/mahamudul-hasan-cse/head-tracking-blink-detection.git
   cd head-tracking-blink-detection
   
3. Install dependencies

pip install -r requirements.txt

4. Run the main application

python MonitorTracking.py

**📸Screenshots**
Here are
F7: Toggle mouse control
F8: Toggle blink Detection
C: Calibrate
Q: Quit
<img width="1287" height="512" alt="Screenshot_3" src="https://github.com/user-attachments/assets/405b889c-a5da-4e22-a2e3-be7d3bd081e6" />

📁 Project Structure
| File/Folder                      | Description                    |
| -------------------------------- | ------------------------------ |
| `MonitorTracking.py`             | Main application               |
| `test_blink_detection.py`        | Blink detection test utility   |
| `CursorCircle.py`                | Visual cursor overlay          |
| `test_camera.py`                 | Camera test utility            |
| `run_head_tracking.bat`          | Batch file runner              |
| `run_head_tracking.ps1`          | PowerShell runner              |
| `run_head_tracking_improved.bat` | Improved batch file runner     |
| `stop_head_tracking.bat`         | Script to stop application     |
| `run_project.py`                 | Alternative Python runner      |
| `run_project_improved.py`        | Improved Python runner         |
| `BLINK_DETECTION_README.md`      | Detailed blink detection guide |
| `requirements.txt`               | Python dependencies            |
| `README.md`                      | Main documentation             |
| `LICENSE`                        | MIT License                    |
| `.gitignore`                     | Ignore unnecessary files       |


🔧 Troubleshooting
Common Issues

| Issue                                    | Possible Fix                                                                  |
| ---------------------------------------- | ----------------------------------------------------------------------------- |
| **Head tracking not working**            | Ensure proper lighting, check camera permissions, confirm webcam is detected. |
| **Blink detection too sensitive**        | Increase `EYE_AR_THRESH` (e.g., `0.25`).                                      |
| **Blink detection not sensitive enough** | Decrease `EYE_AR_THRESH` (e.g., `0.18`).                                      |
| **Cursor movement too fast/slow**        | Adjust `yawDegrees` and `pitchDegrees` in the configuration.                  |
| **Camera feed lagging**                  | Close other applications using the camera to free resources.                  |


📊 Technical Details
Eye Aspect Ratio (EAR)

| Feature/Module              | Description                                                                                                                                                                                                                    |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Blink Detection**         | Uses 6 facial landmarks around each eye for precise blink detection. Compares vertical and horizontal eye distances to determine a blink.                                                                                      |
| **Head Tracking Algorithm** | Detect facial landmarks using MediaPipe Face Mesh. Extract 3D facial coordinates (yaw, pitch, roll). Map head movement to screen coordinates. Apply smoothing filters to reduce jitter. Control mouse movement with PyAutoGUI. |


🛠 Dependencies

| Library           | Purpose                          |
| ----------------- | -------------------------------- |
| **opencv-python** | Video capture & image processing |
| **mediapipe**     | Face mesh detection              |
| **numpy**         | Mathematical operations          |
| **pyautogui**     | Mouse control                    |
| **keyboard**      | Hotkey detection                 |


Install all with:

pip install -r requirements.txt

🤝 Contributing
| Step | Description / Command                                                           |
| ---- | ------------------------------------------------------------------------------- |
| 1    | Fork the repository                                                             |
| 2    | Create a new branch: <br>`git checkout -b feature-name`                         |
| 3    | Commit your changes: <br>`git commit -m "Add new feature"`                      |
| 4    | Push to your fork and create a Pull Request: <br>`git push origin feature-name` |

---
