# python 3.8.5
# opencv 4.4.0
# ghi chú : + nhấn phím 'd' để hiện background .
#           + nhấn phím 'r' để khỏi tạo một background mới
#           + nhấn phím 'q' khi muốn kết thúc
import cv2
import numpy as np
video = cv2.VideoCapture(0)
success, ref_img = video.read()
flag = 0

while(1):
        success, img = video.read()
        if flag==0:
                ref_img = img
        diff1=cv2.subtract(img,ref_img)
        diff2=cv2.subtract(ref_img,img)
        diff = diff1+diff2
        diff[abs(diff)<13.0]=0
        # diff[abs(diff) < 5] = 0
        #gray = diff
        gray = cv2.cvtColor(diff.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        gray[np.abs(gray) < 10] = 0
        fgmask = gray.astype(np.uint8)
        fgmask[fgmask>0]=225
        fgimg = cv2.bitwise_and(img,img,mask = fgmask)
        kernel = np.ones((5,5), np.uint8)
        fgimg_eroded=cv2.erode(fgimg,kernel, iterations=1)
        #ret, jpeg = cv2.imencode('.png', fgimg_eroded)
        cv2.imshow('Edges',fgimg_eroded)
        key = cv2.waitKey(5) & 0xFF
        if ord('q') == key:
                break
        elif ord('d') == key:
                flag = 1
                print("Background black")
        elif ord('r') == key:
                flag = 0
                print("create new background")

cv2.destroyAllWindows()
video.release()












