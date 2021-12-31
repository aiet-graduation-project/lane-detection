import cv2
import numpy as np

# read the input video
cap = cv2.VideoCapture("test2.mp4")




def detect_lane(image):
    # convert current frame into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # apply canny function on the grayscale image
    canny = cv2.Canny(gray, 50, 150)
    return canny


# show the ouptut video
while cap.isOpened():
    # Capture video frames
    _, frame = cap.read()
    # take a copy from current frame
    lane_image = frame
    result = detect_lane(lane_image)
    # show the output frame
    cv2.imshow('result', result)
    # break the loop when the Q key pressed
    if cv2.waitKey(1) == ord('q'):
        break
# close output windows
cap.release()
cv2.destroyAllWindows()
