#! /usr/bin python
# -
# hi frnds  have a fun .....vijesh 
import cv2

# classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

vijesh = cv2.imread('steve.jpg')

gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
# 
yuz_detect = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in yuz_detect:
    cv2.rectangle(resim, (x, y), (x+w, y+h), (255, 0, 0), 2)
   # 
   #
   # 
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = resim[y:y+h, x:x+w]
    goz_detect = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in goz_detect :
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)

cv2.imshow('Face & Eye Detection', vijesh )

cv2.waitKey(0)
cv2.destroyAllWindows()



