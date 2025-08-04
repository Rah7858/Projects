# import cv2

# a = cv2.CascadeClassifier("D:\\Projects\\Face Detection\\haarcascade_frontalface_default.xml")
# b = cv2.VideoCapture(0)

# if not b.isOpened():
#     b = cv2.VideoCapture(1)

# b.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# while True :
#     print("Attempting to capture image...")
#     c_rec, d_image = b.read()
#     print(f"Capture Status: {c_rec}")

#     if not c_rec:
#         print("Failed to Capture image")
#         break
    
#     e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
#     f = a.detectMultiScale(e, 1.3, 6)

#     for (x1, y1, w1, h1 ) in f:
#         cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (0, 255 , 0) , 5)

#         cv2.imshow('img' , d_image)
#         h = cv2.waitKey(40) & 0xFF 
#         if h == ord('q'):
#             break

#         b.release()
#         cv2.destroyAllWindows()

# print(cv2.__version__)
import cv2

# Load the Haar Cascade for face detection
a = cv2.CascadeClassifier("D:\\Projects\\Face Detection\\haarcascade_frontalface_default.xml")
b = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not b.isOpened():
    b = cv2.VideoCapture(1)

# Set video properties
b.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

# Start capturing images
while True:
    c_rec, d_image = b.read()
    
    if not c_rec:
        print("Failed to Capture image")
        break
    
    # Convert to grayscale for face detection
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3, 6)

    # Draw rectangles around detected faces
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 10)

    # Show the image with detected faces
    cv2.imshow('img', d_image)
    
    # Wait for a key press; exit if 'q' is pressed
    h = cv2.waitKey(40) & 0xFF 
    if h == ord('q'):  # Use 'q' to quit
        break

# Release the camera and destroy all windows after exiting the loop
b.release()
cv2.destroyAllWindows()

# Print OpenCV version
print(cv2.__version__)