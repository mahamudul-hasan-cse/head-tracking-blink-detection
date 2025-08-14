# Head Tracking Project

A Python application that uses your webcam to control the mouse cursor based on head movements.

## 🚀 Quick Start

### Option 1: Easy Launcher (Recommended)
Double-click one of these files:
- `run_head_tracking.bat` (Windows)
- `run_head_tracking.ps1` (PowerShell)
- `run_project.py` (Python launcher)

### Option 2: Manual Start
1. Open Command Prompt or PowerShell
2. Navigate to the project folder
3. Run: `python MonitorTracking.py`
4. Open a new terminal and run: `python CursorCircle.py`

## 📋 Requirements

The following packages are required:
- opencv-python
- mediapipe
- numpy
- pyautogui
- keyboard
- PyQt5

## 🔧 Installation

### If using Virtual Environment (Python 3.11+):
```bash
# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install opencv-python mediapipe numpy pyautogui keyboard PyQt5
```

### If using System Python:
The system Python should already have all dependencies installed.

## 🎮 Controls

- **F7**: Toggle mouse control on/off
- **C**: Calibrate (press when looking straight at monitor center)
- **Q**: Quit the application

## 💡 Tips

1. **Camera Issues**: If the wrong camera is used, change `cv2.VideoCapture(1)` to `cv2.VideoCapture(0)` in `MonitorTracking.py`
2. **Lighting**: Ensure your face is well-lit and clearly visible
3. **Calibration**: Use the 'C' key to calibrate when looking straight ahead
4. **Sensitivity**: The system maps 20° horizontal and 10° vertical head movement to full screen

## 🛑 How to Stop

- Press **Q** in the camera window
- Close the camera windows
- Press **Ctrl+C** in the terminal
- Use Task Manager to end `python.exe` processes

## 🔍 Troubleshooting

### "No module named 'mediapipe'" Error
- Use system Python instead of virtual environment
- Or install mediapipe: `pip install mediapipe`

### Camera Not Working
- Try changing camera index in code: `cv2.VideoCapture(0)` or `cv2.VideoCapture(1)`
- Ensure webcam is not used by another application

### Face Detection Issues
- Improve lighting
- Face the camera directly
- Ensure face is clearly visible

## 📁 Files

- `MonitorTracking.py`: Main head tracking application
- `CursorCircle.py`: Cursor overlay display
- `run_head_tracking.bat`: Windows batch launcher
- `run_head_tracking.ps1`: PowerShell launcher
- `run_project.py`: Python launcher
- `README_Updated.md`: This file


