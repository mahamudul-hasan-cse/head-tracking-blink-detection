import cv2
import time

def test_camera(camera_index):
    print(f"Testing camera index {camera_index}...")
    cap = cv2.VideoCapture(camera_index)
    
    if not cap.isOpened():
        print(f"❌ Camera index {camera_index} is not available")
        return False
    
    print(f"✅ Camera index {camera_index} is working!")
    
    # Try to read a frame
    ret, frame = cap.read()
    if ret:
        print(f"✅ Successfully captured frame from camera {camera_index}")
        print(f"   Frame size: {frame.shape}")
        
        # Show the frame briefly
        cv2.imshow(f'Camera Test - Index {camera_index}', frame)
        cv2.waitKey(2000)  # Show for 2 seconds
        cv2.destroyAllWindows()
        
        cap.release()
        return True
    else:
        print(f"❌ Could not read frame from camera {camera_index}")
        cap.release()
        return False

def main():
    print("🎥 Camera Test")
    print("=" * 30)
    
    # Test camera indices 0 and 1
    working_cameras = []
    
    for i in range(2):
        if test_camera(i):
            working_cameras.append(i)
    
    print("\n" + "=" * 30)
    if working_cameras:
        print(f"✅ Working cameras found: {working_cameras}")
        print(f"💡 Use camera index {working_cameras[0]} in MonitorTracking.py")
        
        # Update the MonitorTracking.py file
        if working_cameras[0] != 1:
            print(f"🔄 Updating MonitorTracking.py to use camera index {working_cameras[0]}")
            try:
                with open('MonitorTracking.py', 'r') as f:
                    content = f.read()
                
                content = content.replace('cv2.VideoCapture(1)', f'cv2.VideoCapture({working_cameras[0]})')
                
                with open('MonitorTracking.py', 'w') as f:
                    f.write(content)
                
                print("✅ MonitorTracking.py updated successfully!")
            except Exception as e:
                print(f"❌ Could not update file: {e}")
    else:
        print("❌ No working cameras found!")
        print("💡 Check if your webcam is connected and not being used by another application")

if __name__ == "__main__":
    main()

