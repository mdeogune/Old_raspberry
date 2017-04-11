from picamera import PiCamera
cam=PiCamera()
cam.capture("img.jpg")
import cv2
im=cv2.imread("img.jpg")
cv2.imshow('im',im)
cv2.waitKey(0)
