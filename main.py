from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open video
cap = cv2.VideoCapture("test_video.mp4")

while True:
    success, frame = cap.read()

    if not success:
        break

    # Detect and track objects
    results = model.track(
        frame,
        persist=True,
        verbose=False
    )

    # Draw bounding boxes, labels and tracking IDs
    annotated_frame = results[0].plot()

    # Display result
    cv2.imshow("Object Detection and Tracking", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
