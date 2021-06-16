import cv2
from serial_host import Sender

s = Sender()

camera = cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('image')
cv2.createTrackbar('pan','image',0,180,nothing)
cv2.createTrackbar('tilt','image',0,180,nothing)

while True:
    ret, frame = camera.read()
    
    # show window frame contain live camera video
    cv2.imshow("image", frame)

    # wait for key every 1 millisecond
    key = cv2.waitKey(1)

    # if keyboard key "q" pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # get current positions of  trackbar
    tilt_angle = cv2.getTrackbarPos('tilt','image')
    pan_angle = cv2.getTrackbarPos('pan','image')
    s.send(f"TILT:{tilt_angle};PAN:{pan_angle}")

s.close()
camera.release()
cv2.destroyAllWindows()

    
