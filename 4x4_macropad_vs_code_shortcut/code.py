import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

# The pins we'll use
keypress_pins = [
    board.GP6,
    board.GP5,
    board.GP4, 
    board.GP3, 
    board.GP10,
    board.GP9,
    board.GP8,
    board.GP7,
    board.GP21,
    board.GP20,
    board.GP19,
    board.GP18,
    board.GP16,
    board.GP17,
    board.GP12,
    board.GP11
    ]


# Our array of key objects
key_pin_array = []

# Make all pin objects inputs with pull down
for pin in keypress_pins:
    key_pin = digitalio.DigitalInOut(pin)
    key_pin.switch_to_input(pull=digitalio.Pull.UP)
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

clk = digitalio.DigitalInOut(CLK_PIN)
clk.direction = digitalio.Direction.INPUT
clk.pull = digitalio.Pull.UP

dt = digitalio.DigitalInOut(DT_PIN)
dt.direction = digitalio.Direction.INPUT
dt.pull = digitalio.Pull.UP

sw = digitalio.DigitalInOut(SW_PIN)
sw.direction = digitalio.Direction.INPUT
sw.pull = digitalio.Pull.UP



def ccw():
    print("CCW")
    time.sleep(0.2)
    keyboard.press(control_key, Keycode.MINUS)
    keyboard.release_all()
        
def cw():
    print("CW")
    time.sleep(0.2)
    keyboard.press(control_key, Keycode.EQUALS)
    keyboard.release_all()

def millis():
    return time.monotonic() * 1000

previousValue = True

while True:
    try:
        # ROTARY ENCODER FUNCTIONS
        if previousValue != clk.value:
            if clk.value == False:
                if dt.value:
                    cw()
                    time.sleep(0.3)
                else:
                    ccw()
                    time.sleep(0.3)

        previousValues = clk.value 
        
        if not sw.value:
            print("rot pressed!")
            keyboard.press(control_key, Keycode.ZERO)
            keyboard.release_all()


        # Sadly, python dont have switch case :(
        for i in range(len(key_pin_array)):
            if not key_pin_array[i].value:
                print(f"Key {i} pressed!")
                if i == 0:
                    keyboard.press(control_key, Keycode.K, Keycode.W)
                if i == 1:
                    keyboard.press(control_key, Keycode.GRAVE_ACCENT)
                if i == 2:
                    keyboard.press(control_key, shift_key, Keycode.FIVE)
                if i == 3:
                    keyboard.press(control_key, Keycode.BACKSLASH)
                if i == 4:
                    keyboard.press(control_key, Keycode.F)
                if i == 5:
                    keyboard.press(control_key, Keycode.H)
                if i == 6:
                    keyboard.press(control_key, shift_key, Keycode.F)
                if i == 7:
                    keyboard.press(control_key, Keycode.P)
                if i == 8:
                    keyboard.press(control_key, Keycode.G)
                if i == 9:
                    keyboard.press(alt_key, shift_key, Keycode.TAB)
                if i == 10:
                    keyboard.press(control_key, Keycode.B)
                if i == 11:
                    keyboard.press(alt_key, Keycode.UP_ARROW)
                if i == 12:
                    keyboard.press(control_key, Keycode.FORWARD_SLASH)
                if i == 13:
                    keyboard.press(control_key, shift_key, Keycode.LEFT_ARROW)
                if i == 14:
                    keyboard.press(control_key, shift_key, Keycode.RIGHT_ARROW)
                if i == 15:
                    keyboard.press(alt_key, Keycode.DOWN_ARROW)
                
                keyboard.release_all()
                time.sleep(0.3)
    except KeyboardInterrupt:
        # because we dont want to stop the keyboard function once we try Ctrl+C
        pass
