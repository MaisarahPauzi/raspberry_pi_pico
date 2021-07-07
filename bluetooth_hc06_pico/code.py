# upload latest circuitpython lib "adafruit_bus_device" -> lib folder
import busio
import board

# RX at HC-06 -> GP0 
# TX at HC-06 -> GP1
uart = busio.UART(board.GP0, board.GP1, baudrate=9600)

while True:
    # reading bluetooth serial data
    data = uart.read(32)
    if data is not None:
        data_string = ''.join([chr(b) for b in data])
        print(data_string, end="")