import cv2
import mediapipe as mp
import numpy as np
import handTrackingModule as htm
import autopy   # used to control the mouse
import time

webcam_width, webcam_height = 640, 480
screen_width, screen_height = autopy.screen.size()
frameReduction = 100  # to reduce the area for moving the mouse
smoothening = 7  # to smoothen the mouse movement
prevLoc_x, prevLoc_y = 0, 0
curLoc_x, curLoc_y = 0, 0

length_threshold = 30  # threshold for clicking action

video_cap = cv2.VideoCapture(0)
video_cap.set(3, webcam_width)
video_cap.set(4, webcam_height)

# Creating an object of handDetector class
handDectector = htm.handDetector(maxHands=1, detectionConfidence=0.85)

while True:
    success, image = video_cap.read()
    if not success:
        break

    # display the landmarks
    image = handDectector.findHands(image)

    # get the positions of the landmarks
    lmList = handDectector.findPosition(image, draw=False)

    if len(lmList) != 0:

        fingersUpOrClosedList = handDectector.trackingFingersUpOrClosed(image, lmList)

        # Check whether the index and middle fingers are up
        isIndexFingerUp = fingersUpOrClosedList[1] == 1
        isMiddleFingerUp = fingersUpOrClosedList[2] == 1

        # Reduced frame area for better control of the mouse and hand detection
        cv2.rectangle(image, (frameReduction, frameReduction), (webcam_width - frameReduction, webcam_height - frameReduction), (255, 0, 255), 2)

        # if index finger is up and middle finger is down -> move the mouse
        if isIndexFingerUp and not isMiddleFingerUp:
            # Get the position of the index finger
            index_x, index_y = lmList[8][1:-1]

            # Convert coordinates from webcam to the computer screen size
            try:
                mouse_x = np.interp(index_x, (frameReduction, webcam_width - frameReduction), (0, screen_width))
                mouse_y = np.interp(index_y, (frameReduction, webcam_height - frameReduction), (0, screen_height))

                # Smoothen values
                curLoc_x = prevLoc_x + (mouse_x - prevLoc_x) / smoothening
                curLoc_y = prevLoc_y + (mouse_y - prevLoc_y) / smoothening

                # Move mouse
                autopy.mouse.move(screen_width - curLoc_x, curLoc_y)
                cv2.circle(image, (index_x, index_y), 15, (255, 0, 255), 2)

                # Update previous location
                prevLoc_x, prevLoc_y = curLoc_x, curLoc_y

            except ValueError:
                # Skip mouse movement if point is out of bounds
                pass
 
        # if the index and middle fingers are up -> clicking mode
        elif isIndexFingerUp and isMiddleFingerUp:
            # Get the positions of the index and middle fingers
            index_x, index_y = lmList[8][1:-1]
            middle_x, middle_y = lmList[12][1:-1]

            # if the distance between the index and the middle finger is less than certain value -> click detected
            length, image, ptsList = handDectector.findDistance(8, 12, image, lmList, radius=8, thickness=2)
                
            # click mouse if distance < threshold
            if length < length_threshold:
                cv2.circle(image, (ptsList[4], ptsList[5]), 10, (0, 255, 0), cv2.FILLED)

                autopy.mouse.click()

    

    cv2.imshow("Virtual Mouse", image)
    cv2.waitKey(1)


