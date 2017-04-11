import io
import time
import picamera
import picamera.array
import numpy as np
import cv2
global x
global y
global z
global c_img
import scipy.misc
##from __future__ import print_function
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import time
import cv2
y = z = float(300)
x=0


def cv_size(img):
    return tuple(img.shape[1::-1])
def wrap_image(x,y,z):
    dst = np.array([
	[0, 0],
	[x,100],
	[y,100],
	[300,0]], dtype = "float32")
    return dst

def warp_displayImage():
    dst = wrap_image(x,y,z)
    #dst = cv2.cv.CreateImage(cv_size(c_img), cv2.cv.IPL_DEPTH_8U, 3)
    h,w=300,100
    #rect = np.zeros((4, 2), dtype = "float32")
    rect=np.array([[0,0],[0,w],[h,w],[h,0]],dtype = "float32")
    M = cv2.getPerspectiveTransform(rect, dst)
    warp = cv2.warpPerspective(c_img, M, (300, 100))
    #cv2.cv.WarpPerspective(cv.fromarray(c_img), dst, H2)
##    cv2.imshow('crop',warp)
    return warp
def draw_line(img,lines):
    try:
        i=1
        for line in lines:
            for i in range(0,len(line)):
                       
                coord=line[i]
                
                cv2.line(img,(coord[0],coord[1]),(coord[2],coord[3]),[255,255,255],3)
    except:
        pass
def process_img(p_img):
    
    p_img =scipy.misc.imresize(p_img,30,interp='bilinear',mode=None)
    p_img=cv2.cvtColor(p_img,cv2.COLOR_BGR2GRAY)
    p_img=cv2.Canny(p_img,threshold1=100,threshold2=150)
    p_img=cv2.GaussianBlur(p_img,(5,5),1)
    #vertices = np.array([[[10,360],[10,260],[200,220],[400,220],[600,260],[600,360],
                         #]], np.int32)
    #vertices=np.array([[[0,360],[0,360],[30,20],[30,30]]],np.int32)
    #p_img=roi(p_img,vertices)
    lines=cv2.HoughLinesP(p_img,1,np.pi/90,100,np.array([]),1,1)
##    try:
##        l1, l2 = draw_lanes(p_img,lines)
##        cv2.line(p_img, (l1[0], l1[1]), (l1[2], l1[3]), [0,255,0], 30)
##        cv2.line(p_img, (l2[0], l2[1]), (l2[2], l2[3]), [0,255,0], 30)
##    except Exception as e:
      #  print(str(e))
##        pass
##    try:
##        for coords in lines:
##            coords = coords[0]
##            try:
##                cv2.line(processed_img, (coords[0], coords[1]), (coords[2], coords[3]), [255,0,0], 3)
##                
##                
##            except Exception as e:
##                print(str(e))
##    except Exception as e:
##        pass
    draw_line(p_img,lines)
    return p_img
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 80
rawCapture = PiRGBArray(camera, size=(320, 240))
stream = camera.capture_continuous(rawCapture, format="bgr",
	use_video_port=True)

stream.close()
rawCapture.close()
camera.close()
vs = PiVideoStream().start()
time.sleep(2.0)
fps = FPS().start()
finish = time.time()
while True:
    
        
    
    frame = vs.read()
    
##    frame = imutils.resize(frame, width=300,height=300)
    ##        cv2.imshow('frame',frame1)

    c_img=frame[150:250,:]
##    frame=warp_displayImage()
    p_img=process_img(c_img)
##    cv2.imshow('edge',p_img)
##    if cv2.waitKey(1)& 0xFF == ord('q'):
##            break
        # How fast were we?
    
    print('Captured 40 images at %.2ffps' % ( 1/(time.time()-finish )))
    finish = time.time()
    fps.update()

fps.stop()
cv2.waitKey(0)& 0xFF == ord('q')
cv2.destroyAllWindows()
vs.stop()
