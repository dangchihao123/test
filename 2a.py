# python 3.8.5
# opencv 4.4.0
import cv2
video = cv2.VideoCapture(0)
a = 0
while True:

    a = a + 1
    check, frame = video.read()
    # thay đổi kích thước khung
    frame = cv2.resize(frame, (152, 228))
    print(frame.shape)
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
showPic = cv2.imwrite("filename1.jpg",frame)
print(showPic)
video.release()
cv2.destroyAllWindows

