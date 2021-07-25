# upload latest circuitpython lib "adafruit_bus_device" -> lib folder
import busio
import board
import pwmio
from adafruit_motor import motor


# Motors Setup
PWM_PIN_A1 = board.GP8  
PWM_PIN_A2 = board.GP9

PWM_PIN_B1 = board.GP10  
PWM_PIN_B2 = board.GP11


pwm_a1 = pwmio.PWMOut(PWM_PIN_A1, frequency=50)
pwm_a2 = pwmio.PWMOut(PWM_PIN_A2, frequency=50)
pwm_b1 = pwmio.PWMOut(PWM_PIN_B1, frequency=50)
pwm_b2 = pwmio.PWMOut(PWM_PIN_B2, frequency=50)
motor1 = motor.DCMotor(pwm_a1, pwm_a2)
motor2 = motor.DCMotor(pwm_b1, pwm_b2)

def forward():
    motor1.throttle = 0.5
    motor2.throttle = 0.5


def backward():
    motor1.throttle = -0.5
    motor2.throttle = -0.5


def stop():
    motor1.throttle = 0
    motor2.throttle = 0


def left():
    motor1.throttle = -0.5
    motor2.throttle = 0


def right():
    motor1.throttle = 0
    motor2.throttle = -0.5

# RX at HC-06 -> GP0 
# TX at HC-06 -> GP1
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)
print("START BT")
while True:
    # reading bluetooth serial data
    data = uart.read(32)
    if data is not None:
        data_string = ''.join([chr(b) for b in data])

        if data_string == '0000004#':
            forward()
        elif data_string == '0000003#':
            right()
        elif data_string == '0000002#':
            backward()
        elif data_string == '0000001#':
            left()
        else:
            stop()
    else:
        stop()