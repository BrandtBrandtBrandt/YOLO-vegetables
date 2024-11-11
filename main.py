import os
import cv2
from ultralytics import YOLO

# Change the working directory to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
# Load the YOLO model
model = YOLO("./best_yolov11s_500epochs.pt")


# Capture from the external camera (input 1)
cap = cv2.VideoCapture(1, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform YOLO inference (tracking)
    results = model(frame)

    # Display the frame with YOLO results
    annotated_frame = results[0].plot()  # YOLO draws the bounding boxes on the frame
    cv2.imshow('YOLOv11 Tracking', annotated_frame)

    # Press 'q' to break the loop and close the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()