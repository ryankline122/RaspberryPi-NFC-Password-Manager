import cv2

# Open the default camera
cap = cv2.VideoCapture(1)

# Capture one frame from the camera
ret, frame = cap.read()

# Check if the frame was captured successfully
if ret:
    # Save the captured frame to a file
    cv2.imwrite('captured_image.jpg', frame)
    print("Image saved successfully!")
else:
    print("Failed to capture image.")

# Release the camera
cap.release()