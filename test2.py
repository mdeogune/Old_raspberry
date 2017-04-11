import io
import picamera
import time
import cv2
import numpy as np
st=io.BytesIO()

with picamera.PiCamera() as camera:
    ##    camera.start_preview()
##        time.sleep(2)
    
    while True:
        st=io.BytesIO()
        camera.capture(st,format='jpeg')
        data=np.fromstring(st.getvalue(),dtype=np.uint8)
        image=cv2.imdecode(data,1)
        cv2.imshow('im',image)
        if cv2.waitKey(1)& 0xFF == ord('q'):
            break
cv2.waitKey(0)& 0xFF == ord('q')
cv2.destroyAllWindows()

