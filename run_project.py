#!/usr/bin/env python3
"""
Head Tracking Project Launcher
This script runs both the head tracking and cursor overlay programs.
"""

import subprocess
import sys
import time
import os

def main():
    print("🎯 Head Tracking Project Launcher")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("MonitorTracking.py"):
        print("❌ Error: MonitorTracking.py not found!")
        print("Please run this script from the project directory.")
        return
    
    print("🚀 Starting Head Tracking Project...")
    print()
    
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
        print("⏹️  To stop: Press Ctrl+C in this window or close the camera windows")
        print()
        
        # Wait for user to stop
        try:
            while True:
                time.sleep(1)
                # Check if processes are still running
                if tracking_process.poll() is not None:
                    print("❌ MonitorTracking.py has stopped")
                    break
                if cursor_process.poll() is not None:
                    print("❌ CursorCircle.py has stopped")
                    break
                    
        except KeyboardInterrupt:
            print("\n🛑 Stopping programs...")
            
    except Exception as e:
        print(f"❌ Error starting programs: {e}")
        return
    
    finally:
        # Clean up processes
        try:
            if 'tracking_process' in locals():
                tracking_process.terminate()
            if 'cursor_process' in locals():
                cursor_process.terminate()
            print("✅ Programs stopped successfully")
        except:
            pass

if __name__ == "__main__":
    main()

