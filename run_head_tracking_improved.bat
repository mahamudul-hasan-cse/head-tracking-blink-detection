@echo off
echo ========================================
echo    Head Tracking Project Launcher
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Starting Head Tracking Project...
echo.

REM Kill any existing Python processes that might be running the scripts
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im pythonw.exe >nul 2>&1

echo Running MonitorTracking.py...
start "Head Tracking" cmd /k "python MonitorTracking.py"

echo Running CursorCircle.py...
start "Cursor Overlay" cmd /k "python CursorCircle.py"

echo.
echo ========================================
echo    Both scripts are now running!
echo ========================================
echo.
echo Controls:
echo - F7: Toggle mouse control on/off
echo - C: Calibrate when looking straight ahead
echo - Q: Quit the application
echo.
echo To stop the project:
echo 1. Press Q in the camera window, OR
echo 2. Close the camera windows, OR
echo 3. Press any key in this window to force stop
echo.
echo ========================================
pause

echo.
echo Stopping all processes...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im pythonw.exe >nul 2>&1
echo All processes stopped.
echo.
pause



