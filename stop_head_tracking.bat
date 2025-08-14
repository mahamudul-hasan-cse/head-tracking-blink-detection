@echo off
echo ========================================
echo    Stopping Head Tracking Project
echo ========================================
echo.

echo Stopping all Python processes...
taskkill /f /im python.exe >nul 2>&1
taskkill /f /im pythonw.exe >nul 2>&1

echo.
echo Checking for any remaining processes...
tasklist /fi "imagename eq python.exe" 2>nul | find "python.exe" >nul
if %errorlevel% equ 0 (
    echo Force killing remaining Python processes...
    taskkill /f /im python.exe >nul 2>&1
) else (
    echo No Python processes found.
)

echo.
echo ========================================
echo    All processes stopped!
echo ========================================
echo.
echo The green cursor overlay should now be gone.
echo.
pause



