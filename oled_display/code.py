import time
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306


displayio.release_displays()

i2c_oled = busio.I2C(scl=board.GP5, sda=board.GP4)
display_bus = displayio.I2CDisplay(i2c_oled, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

print("START")

# Make the display context
text_group = displayio.Group(max_size=10)

# Draw a label
text = "JOYSTICK START IN 2s"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=4)
text_group.append(text_area)

display.show(text_group)
time.sleep(2)
text_group.pop()

while True:
    pass