import cv2
import numpy as np

# read the input video
cap = cv2.VideoCapture("test2.mp4")


def region_of_interest(image):
    # return the height of the image
    height = image.shape[0]
    # set region vertices
    triangle = np.array([[(200, height), (1100, height), (550, 250)]])
    # Return an array of zeros with the same shape and type as a given array
    mask = np.zeros_like(image)
    # fill the black mask with the region triangle
    cv2.fillPoly(mask, triangle, 255)
    # apply and on the mask image to crop the region of interest only
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def detect_lane(image):
    # convert current frame into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # apply canny function on the grayscale image
    canny = cv2.Canny(gray, 50, 150)
    # define the interest region
    cropped_image = region_of_interest(canny)
    return cropped_image


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
