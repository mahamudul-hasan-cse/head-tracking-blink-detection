# Eye Blink Detection for Head Tracking Project

## Overview
The head tracking project now includes eye blink detection functionality that allows you to click the mouse by blinking your eyes. This feature works alongside the existing head movement tracking for complete hands-free mouse control.

## Features Added

### 1. Eye Blink Detection
- **EAR (Eye Aspect Ratio) Calculation**: Uses MediaPipe face landmarks to calculate the aspect ratio of your eyes
- **Blink Detection**: Detects when you blink based on a configurable threshold
- **Mouse Clicking**: Automatically clicks the mouse when a blink is detected
- **Cooldown System**: Prevents accidental clicks with a 0.5-second cooldown between blinks

### 2. Visual Feedback
- **Eye Landmarks**: Yellow dots show the detected eye landmarks
- **EAR Display**: Real-time display of your eye aspect ratio
- **Blink Counter**: Shows how many consecutive frames your eyes are closed
- **Status Indicators**: Shows whether mouse control and blink detection are enabled

### 3. Controls
- **F7**: Toggle mouse movement control on/off
- **F8**: Toggle blink detection on/off
- **C**: Calibrate head tracking (recenter)
- **Q**: Quit the application

## How It Works

### Eye Aspect Ratio (EAR)
The system calculates the EAR using 6 key landmarks around each eye:
- Measures vertical distances between upper and lower eyelids
- Measures horizontal distance between eye corners
- EAR = (vertical1 + vertical2) / (2 × horizontal)

### Blink Detection Logic
1. When EAR drops below threshold (0.21), blink counter increases
2. When EAR rises above threshold, if counter ≥ 2 frames, blink is detected
3. Mouse clicks only if both mouse control and blink detection are enabled
4. 0.5-second cooldown prevents rapid-fire clicking

## Configuration

### Adjustable Parameters
You can modify these values in `MonitorTracking.py`:

```python
EYE_AR_THRESH = 0.21          # Lower = more sensitive to blinks
EYE_AR_CONSEC_FRAMES = 2      # Frames eyes must be closed
blink_cooldown = 0.5          # Seconds between clicks
```

### Sensitivity Tuning
- **Too sensitive**: Lower `EYE_AR_THRESH` (e.g., 0.18)
- **Not sensitive enough**: Raise `EYE_AR_THRESH` (e.g., 0.25)
- **Too many false clicks**: Increase `EYE_AR_CONSEC_FRAMES` (e.g., 3)
- **Want faster clicking**: Decrease `blink_cooldown` (e.g., 0.3)

## Usage Instructions

1. **Run the main application**:
   ```bash
   python MonitorTracking.py
   ```

2. **Test blink detection** (optional):
   ```bash
   python test_blink_detection.py
   ```

3. **Setup**:
   - Ensure good lighting on your face
   - Position yourself so your eyes are clearly visible
   - Press 'C' to calibrate head tracking
   - Press 'F8' to enable blink detection

4. **Using the system**:
   - Move your head to control mouse cursor position
   - Blink to click the mouse
   - Use F7/F8 to toggle features as needed

## Troubleshooting

### Blink Detection Not Working
- Check lighting conditions
- Ensure eyes are clearly visible to camera
- Adjust `EYE_AR_THRESH` value
- Try the test script first: `python test_blink_detection.py`

### Too Many False Clicks
- Increase `EYE_AR_CONSEC_FRAMES` to 3 or 4
- Increase `blink_cooldown` to 1.0
- Check for camera movement or poor lighting

### Not Sensitive Enough
- Decrease `EYE_AR_THRESH` to 0.18 or 0.19
- Decrease `EYE_AR_CONSEC_FRAMES` to 1
- Ensure you're making deliberate blinks

## Technical Details

### Eye Landmarks Used
- **Left Eye**: [362, 385, 387, 263, 373, 380]
- **Right Eye**: [33, 160, 158, 133, 153, 144]

### Dependencies
- OpenCV (cv2)
- MediaPipe (mediapipe)
- NumPy (numpy)
- PyAutoGUI (pyautogui)
- Keyboard (keyboard)

## Safety Notes
- Take regular breaks to avoid eye strain
- Don't use for extended periods without breaks
- Ensure the system is properly calibrated before use
- Be aware of the cooldown period between clicks
