import cv2

# Initialize camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Bhai, camera nahi khul raha! Check kar.")
    exit()

while True:
    # Read frame from camera
    ret, frame = cap.read()
    if not ret:
        print("Bhai, frame nahi mil raha!")
        break

    # Display the frame
    cv2.imshow('Camera Live', frame)

    # Press 's' to save photo and 'q' to quit
    key = cv2.waitKey(1)
    if key == ord('s'):  # Save photo
        cv2.imwrite('captured_photo.jpg', frame)
        print("Bhai, photo save ho gaya - captured_photo.jpg!")
    elif key == ord('q'):  # Quit
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()