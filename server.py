import cv2 as cv
import imagezmq

frames = 0

image_hub = imagezmq.ImageHub(open_port="tcp://127.0.0.1:5555", REQ_REP=False)
while True:  # show streamed images until Ctrl-C
    rpi_name, image = image_hub.recv_image()
    cv.imshow(rpi_name, image)
    frames += 1
    if frames % 60 == 0:
        print(image.shape, image.size, image.dtype)
    print(frames)

    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindows()
