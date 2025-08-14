Install dependencies using

pip install opencv-python mediapipe numpy pyautogui keyboard

Run script 1:

python MonitorTracking.py

Run script 2 in separate terminal:

python CursorCircle.py

Features:
Press F7 to toggle mouse control on/off.
Press 'c' to calibrate when looking straight at your monitor center.
Press 'q' to quit the application.

If the wrong camera is used, change cv2.VideoCapture(1) to another index, such as cv2.VideoCapture(0)