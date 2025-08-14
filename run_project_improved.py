#!/usr/bin/env python3
"""
Improved Head Tracking Project Launcher
This script runs both the head tracking and cursor overlay programs with proper cleanup.
"""

import subprocess
import sys
import time
import os
import signal
import psutil

def kill_python_processes():
    """Kill any existing Python processes running our scripts"""
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            try:
                if proc.info['name'] in ['python.exe', 'pythonw.exe']:
                    cmdline = proc.info['cmdline']
                    if cmdline and any(script in ' '.join(cmdline) for script in ['MonitorTracking.py', 'CursorCircle.py']):
                        print(f"🔄 Stopping existing process: {proc.info['name']} (PID: {proc.info['pid']})")
                        proc.terminate()
                        proc.wait(timeout=3)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired):
                pass
    except Exception as e:
        print(f"⚠️  Warning: Could not clean up processes: {e}")

def main():
    print("🎯 Improved Head Tracking Project Launcher")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("MonitorTracking.py"):
        print("❌ Error: MonitorTracking.py not found!")
        print("Please run this script from the project directory.")
        return
    
    # Kill any existing processes
    print("🧹 Cleaning up any existing processes...")
    kill_python_processes()
    time.sleep(1)
    
    print("🚀 Starting Head Tracking Project...")
    print()
    
    tracking_process = None
    cursor_process = None
    
    try:
        # Start MonitorTracking.py
        print("📹 Starting MonitorTracking.py...")
        tracking_process = subprocess.Popen([sys.executable, "MonitorTracking.py"])
        
        # Wait a moment for the first process to start
        time.sleep(2)
        
        # Start CursorCircle.py
        print("🖱️  Starting CursorCircle.py...")
        cursor_process = subprocess.Popen([sys.executable, "CursorCircle.py"])
        
        print()
        print("✅ Both programs are now running!")
        print()
        print("🎮 Controls:")
        print("   • F7: Toggle mouse control on/off")
        print("   • C: Calibrate when looking straight ahead")
        print("   • Q: Quit the application")
        print()
        print("💡 Tips:")
        print("   • Make sure your face is well-lit")
        print("   • If camera doesn't work, try changing cv2.VideoCapture(1) to cv2.VideoCapture(0)")
        print("   • Use calibration (C key) when looking straight at monitor center")
        print()
        print("⏹️  To stop: Press Ctrl+C in this window")
        print()
        
        # Wait for user to stop
        try:
            while True:
                time.sleep(1)
                # Check if processes are still running
                if tracking_process and tracking_process.poll() is not None:
                    print("❌ MonitorTracking.py has stopped")
                    break
                if cursor_process and cursor_process.poll() is not None:
                    print("❌ CursorCircle.py has stopped")
                    break
                    
        except KeyboardInterrupt:
            print("\n🛑 Stopping programs...")
            
    except Exception as e:
        print(f"❌ Error starting programs: {e}")
        return
    
    finally:
        # Clean up processes
        print("🧹 Cleaning up processes...")
        try:
            if tracking_process:
                tracking_process.terminate()
                tracking_process.wait(timeout=3)
            if cursor_process:
                cursor_process.terminate()
                cursor_process.wait(timeout=3)
            
            # Force kill any remaining Python processes
            kill_python_processes()
            
            print("✅ All programs stopped successfully")
        except Exception as e:
            print(f"⚠️  Warning during cleanup: {e}")

if __name__ == "__main__":
    main()



