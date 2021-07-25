import time
import board
import pwmio
from adafruit_motor import motor
import pulseio
import adafruit_irremote

# IR Remote Setup
pulsein = pulseio.PulseIn(board.GP7, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()

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

while True:
    pulses = decoder.read_pulses(pulsein)
    try:
        code = decoder.decode_bits(pulses)
        btn_pressed_code = code[-1]
        print(code[-1])
        if btn_pressed_code == 16:
            left()
            time.sleep(1)
            stop()
        elif btn_pressed_code == 24:
            forward()
        elif btn_pressed_code == 90:
            right()
        elif btn_pressed_code == 74:
            backward()
        else:
            stop()
        
    except adafruit_irremote.IRDecodeException as e:     # failed to decode
        print("Failed to decode: ", e.args)
        stop()