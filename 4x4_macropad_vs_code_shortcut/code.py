import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# The pins we'll use
keypress_pins = [
    board.GP12,
    board.GP19,
    board.GP18, 
    board.GP17, 
    board.GP16,
    board.GP21,
    board.GP10,
    board.GP11,
    board.GP9,
    board.GP8,
    board.GP22,
    board.GP20,
    board.GP26,
    board.GP5,
    board.GP7
    ]


# Our array of key objects
key_pin_array = []

# Make all pin objects inputs with pull down
for pin in keypress_pins:
    key_pin = digitalio.DigitalInOut(pin)
    key_pin.switch_to_input(pull=digitalio.Pull.DOWN)
    key_pin_array.append(key_pin)

# common keys
control_key = Keycode.CONTROL
shift_key = Keycode.SHIFT
alt_key = Keycode.LEFT_ALT

time.sleep(1)  # Sleep for a bit to avoid a race condition on some systems


# The keyboard object!
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

# Rotary Encoder Pins
CLK_PIN = board.GP14
DT_PIN = board.GP15
SW_PIN = board.GP13
clk_last = None

clk = digitalio.DigitalInOut(CLK_PIN)
clk.direction = digitalio.Direction.INPUT

dt = digitalio.DigitalInOut(DT_PIN)
dt.direction = digitalio.Direction.INPUT

sw = digitalio.DigitalInOut(SW_PIN)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.DOWN



def ccw():
    print("CCW")
    keyboard.press(control_key, Keycode.MINUS)
    keyboard.release_all()
        
def cw():
    print("CW")
    keyboard.press(control_key, Keycode.EQUALS)
    keyboard.release_all()


while True:
    # ROTARY ENCODER FUNCTIONS
    clkState = clk.value
    if clk_last is not None:
        if(clk_last !=  clkState):
            if(dt.value != clkState):
                cw()
            else:
                ccw()
            
    if not sw.value:
        print("rot pressed!")
        keyboard.press(control_key, Keycode.ZERO)
        keyboard.release_all()
            
    clk_last = clkState

    # KEYBOARD FUNCTIONS
    for i in range(len(key_pin_array)):
        if key_pin_array[i].value:
            # Sadly, python dont have switch case :(
            if i == 0:
                keyboard.press(control_key, Keycode.FORWARD_SLASH)
            if i == 1:
                keyboard.press(control_key, shift_key, Keycode.LEFT_ARROW)
            if i == 2:
                keyboard.press(control_key, shift_key, Keycode.RIGHT_ARROW)
            if i == 3:
                keyboard.press(alt_key, Keycode.UP_ARROW)
            if i == 4:
                keyboard.press(alt_key, Keycode.DOWN_ARROW)
            if i == 5:
                keyboard.press(control_key, Keycode.B)
            if i == 6:
                keyboard.press(alt_key, Keycode.RIGHT_ARROW)
            if i == 7:
                keyboard.press(alt_key, Keycode.LEFT_ARROW)
            if i == 8:
                keyboard.press(control_key, Keycode.F)
            if i == 9:
                keyboard.press(control_key, Keycode.H)
            if i == 10:
                keyboard.press(control_key, shift_key, Keycode.F)
            if i == 11:
                keyboard.press(control_key, Keycode.P)
            if i == 12:
                keyboard.press(control_key, Keycode.BACKSLASH)
            if i == 13:
                keyboard.press(control_key, shift_key, Keycode.FIVE)
            if i == 14:
                keyboard.press(control_key, Keycode.GRAVE_ACCENT)
            
            keyboard.release_all()
            time.sleep(0.3)