import time
import board
import busio
import displayio
import terminalio
import adafruit_ds3231
from adafruit_display_text import label
import adafruit_displayio_ssd1306

print("START")

# setup oled
i2c_oled = busio.I2C(board.GP27, board.GP26)

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c_oled, device_address=60)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

text_group = displayio.Group(max_size=10, scale=3, x=0, y=0)

# setup rtc
i2c_rtc = busio.I2C(board.GP17, board.GP16)
rtc = adafruit_ds3231.DS3231(i2c_rtc)

while True:
    t = rtc.datetime
    text = "{}:{:02}".format(t.tm_hour, t.tm_min)
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFFFF, x=0, y=4)
    text_group.append(text_area)
    display.show(text_group)
    time.sleep(60)
    text_group.pop()

