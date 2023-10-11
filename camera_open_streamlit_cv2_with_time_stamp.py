# pip install opencv-python-headless
import cv2
import streamlit
import datetime

streamlit.title("Ito ang bidyo mo")
istart = streamlit.button('Buksan mo na ang camera')

if istart:
    stream_imahe = streamlit.image([ ])
    kamara = cv2.VideoCapture(1)

    while True:
        tsek, frame = kamara.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        now = datetime.datetime.now()

        cv2.putText(img=frame, text='Hilo', org=(50,50),
                                fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(20,100,200),
                                thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame,
                    text=now.strftime("%m/%d/%Y, %H:%M:%S"),
                    org=(50, 80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        cv2.putText(img=frame,
                    text=now.strftime('%A'),
                    org=(50, 120),
                    fontFace=cv2.FONT_HERSHEY_PLAIN,
                    fontScale=2,
                    color=(20, 100, 200),
                    thickness=2,
                    lineType=cv2.LINE_AA)

        stream_imahe.image(frame)