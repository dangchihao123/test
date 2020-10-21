# python 3.8.5
# opencv 4.4.0
# ghi chú : thủ nghiệm trên nền màu trắng khi webcam được bật lên , có đưa vào sẵn 1 background .
import cv2
import numpy as np
video = cv2.VideoCapture(0)
image = cv2.imread("bg.jpeg")
# video1 = cv2.VideoCapture(1)
flag=0
while True:
        success, img = video.read()
        #success2, bg = oceanVideo.read()
        #bg = resize(bg, ref_img)
        if flag == 0:
                ref_img = img
        ret, frame = video.read()

        frame = cv2.resize(frame, (640, 480))
        image = cv2.resize(image, (640, 480))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        u_green = np.array([255, 255, 255])
        #l_green = np.array([30, 30, 0])
        l_green = np.array([84, 74, 8])

        mask = cv2.inRange(frame, l_green, u_green)
        res = cv2.bitwise_and(frame, frame, mask=mask)

        f = frame - res
        f = np.where(f == 0, image, f)

        cv2.imshow("video", frame)
        cv2.imshow("mask", f)
        key = cv2.waitKey(5) & 0xFF

        if cv2.waitKey(25) == 27:
                break

video.release()
cv2.destroyAllWindows()
