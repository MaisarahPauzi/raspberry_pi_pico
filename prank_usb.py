import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)
# common keys
control_key = Keycode.CONTROL
shift_key = Keycode.SHIFT
alt_key = Keycode.LEFT_ALT
window_key = Keycode.WINDOWS

time.sleep(1)

# The keyboard object!
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

def typing(key):
	keyboard.press(key)
	keyboard.release_all()
	time.sleep(0.3)

typing(window_key)
keyboard_layout.write("txt")
time.sleep(0.3)
typing(Keycode.ENTER)
keyboard_layout.write("Your laptop have been HACKED!!!!!!")
time.sleep(0.3)
