@echo off
echo Starting Head Tracking Project...
echo.
echo Running MonitorTracking.py...
start "Head Tracking" cmd /k "python MonitorTracking.py"
echo.
echo Running CursorCircle.py...
start "Cursor Overlay" cmd /k "python CursorCircle.py"
echo.
echo Both scripts are now running!
echo.
echo Controls:
echo - F7: Toggle mouse control on/off
echo - C: Calibrate when looking straight ahead
echo - Q: Quit the application
echo.
echo Press any key to close this window...
pause >nul
