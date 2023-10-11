import cv2
import time

bidyo = cv2.VideoCapture(1)
time.sleep(1)

if not bidyo.isOpened():
   print("Ayaw mabuksan ang camera, shet")
   exit()

while True:
    check, frame = bidyo.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gaussian = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    cv2.imshow('My bidyo', gray_frame_gaussian)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

bidyo.release()