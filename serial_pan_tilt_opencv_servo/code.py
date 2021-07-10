import supervisor
import time
import board
import pwmio
from adafruit_motor import servo

pwm1 = pwmio.PWMOut(board.GP14, duty_cycle=2 ** 15, frequency=50)
pwm2 = pwmio.PWMOut(board.GP15, duty_cycle=2 ** 15, frequency=50)

tilt_servo = servo.Servo(pwm1)
pan_servo = servo.Servo(pwm2)

while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        # expected text = TILT:180;PAN:90
        splitted_text = value.split(";")
        tilt_text = splitted_text[0]
        tilt_angle = tilt_text.split(":")[1]
        tilt_servo.angle = int(tilt_angle)

        pan_text = splitted_text[1]
        pan_angle = pan_text.split(":")[1]
        pan_servo.angle = int(pan_angle)


        print(f"Tilt Angle: {tilt_angle} Pan Angle: {pan_angle}")
        time.sleep(0.05)