# python 3.8.5
# opencv 4.4.0
# Nhập tất cả các thư viện cần thiết
# 1.Tải hình ảnh hoặc video
# 2.Thay đổi kích thước hình ảnh và video thành cùng kích thước
# 3.Tải các giá trị BGR trên và dưới của màu xanh lục
# 4.Đắp mặt nạ và sau đó sử dụng bitwise_and
# 5.Trừ bitwise_and khỏi hình ảnh màn hình xanh ban đầu
# 6.Kiểm tra giá trị ma trận 0 sau phân số và thay thế nó bằng hình ảnh thứ hai
# 7.Bạn sẽ có được kết quả mong muốn.
# ghi chú : - khi ta dùng áo choàng màu trắng đắp hết lên người thì sẽ biến mất tiêu luôn á chỉ còn lại cái background.
import cv2
import numpy as np
video = cv2.VideoCapture(0)
image = cv2.imread("bg.jpeg")
#video1 = cv2.VideoCapture(1)
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
        # u_green = np.array([151, 145, 72])
        # l_green = np.array([164, 158, 89])
        l_green = np.array([40,60,15])

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
