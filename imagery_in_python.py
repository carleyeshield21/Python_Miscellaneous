import cv2
import time

bidyo = cv2.VideoCapture(0)
time.sleep(1)

while True:
    check, frame = bidyo.read()
    cv2.imshow('My bidyo', frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
bidyo.release()
