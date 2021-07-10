import cv2
import numpy as np
import serial

class Sender:
    TERMINATOR = '\r'.encode('UTF8')

    def __init__(self, device='COM12', baud=115200, timeout=1):
        self.serial = serial.Serial(device, baud, timeout=timeout)

    def receive(self) -> str:
        line = self.serial.read_until(self.TERMINATOR)
        return line.decode('UTF8').strip()

    def send(self, text: str) -> bool:
        line = '%s\r\f' % text
        self.serial.write(line.encode('UTF8'))
        # the line should be echoed.
        # If it isn't, something is wrong.
        return text == self.receive()

    def close(self):
        self.serial.close()

face_clsfr=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

GREEN = (0,255,0)
WHITE = (255,255,255)
p_angle = 50
t_angle = 30
s = Sender()

def move_servo_tilt(angle):
    global t_angle
    if(t_angle > 0 and t_angle <= 180):
        t_angle += angle

def move_servo_pan(angle):
    global p_angle
    if(p_angle > 0 and p_angle <= 180):
        p_angle += angle

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()
    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_clsfr.detectMultiScale(gray,1.3,5)
    # detect faces
    for (x,y,w,h) in faces:
        # draw rectangle to detected face
        cv2.rectangle(frame,(x,y),(x+w,y+h),GREEN,2)
        
        # draw rectange for background of text
        cv2.rectangle(frame,(x,y-40),(x+w,y),GREEN,-1)
        
        # coordinate text
        centre_x = x+int(w/2)
        centre_y = y+int(h/2)
        
        if (centre_x > 0 and centre_x < 250):
            x_direction = 'left'
            move_servo_pan(1)
            
        elif (centre_x >=250 and centre_x < 350):
            x_direction = 'center'
            move_servo_pan(0)
        else:
            x_direction = 'right'
            move_servo_pan(-1)
        
            
        coord_text = f'X direction = {x_direction}'
        
        # put dot in the middle of face
        cv2.circle(frame, (centre_x, centre_y), 7, GREEN, -1)
        
        # draw text of detected face (wear mask or not)
        cv2.putText(frame, coord_text, (x, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.8,WHITE,2)

    # show window frame contain live camera video
    cv2.imshow("Live Camera", frame)

    # wait for key every 1 millisecond
    key = cv2.waitKey(1)

    # if keyboard key "q" pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    move_servo_tilt(0)
    s.send(f"TILT:{t_angle};PAN:{p_angle}")
    
s.close()
camera.release()
cv2.destroyAllWindows()