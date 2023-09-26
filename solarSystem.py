import cv2 
img = cv2.imread("solar-system.jpg")

cv2.waitKey(0)
cv2.putText(img,
"sun",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Mercury",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Venus",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Earth",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Mars",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Jupiter",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Saturn",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Uranus",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))
cv2.putText(img,
"Neptune",(100,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imwrite("Solar-System.jpg",img)

cv2.imsow("output",img)