import time
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

print("START")


i2c_oled = busio.I2C(board.GP27, board.GP26)

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c_oled, device_address=60)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


# Make the display context
text_group = displayio.Group(max_size=10, scale=3, x=0, y=0)

# Draw a label
text = "HELLO!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=4)
text_group.append(text_area)

display.show(text_group)
time.sleep(10)
text_group.pop()

while True:
    pass