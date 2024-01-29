import cv2 as cv
import imagezmq

import time

sender = imagezmq.ImageSender(connect_to="tcp://127.0.0.1:5555", REQ_REP=False)

time.sleep(2.0)

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    sender.send_image("webcam_stream", frame)

cap.release()
cv.destroyAllWindows()
