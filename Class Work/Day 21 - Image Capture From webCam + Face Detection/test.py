import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame = cap.read()
else:
    ret = False
img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

plt.imshow(img)
plt.show()
cv2.imwrite("Captured.jpg",frame)
cap.release() 
