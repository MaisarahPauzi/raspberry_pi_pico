import time
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

time.sleep(5)

while True:
	try:
		mouse.move(x=10)
		time.sleep(0.5)
		mouse.move(x=-10)
		time.sleep(0.5)
	except KeyboardInterrupt:
        # because we dont want to stop the mouse function once we try Ctrl+C
		pass