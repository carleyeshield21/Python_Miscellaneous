import cv2
import time
from camera_main import send_email

bidyo = cv2.VideoCapture(1)
time.sleep(1)

if not bidyo.isOpened():
   print("Ayaw mabuksan ang camera, shet")
   exit()

pers_frame = None
status_list = []

while True:
    status = 0
    check, frame = bidyo.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gaussian = cv2.GaussianBlur(gray_frame, (21, 21), 0)


    if pers_frame is None:
        pers_frame = gray_frame_gaussian

    delta_frame = cv2.absdiff(pers_frame, gray_frame_gaussian)
    threshold_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]
    dilated_frame = cv2.dilate(threshold_frame, None, iterations=2)
    cv2.imshow('My bidyo',dilated_frame)
    contours, check = cv2.findContours(dilated_frame,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)


    for contour in contours:
        if cv2.contourArea(contour) < 10000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
        if rectangle.any():
            status = 1
            send_email()

    status_list.append(status)
    status_list = status_list[-2:]

    cv2.imshow('bidyo2', frame)

    # print(delta_frame)
    print(status_list)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

bidyo.release()