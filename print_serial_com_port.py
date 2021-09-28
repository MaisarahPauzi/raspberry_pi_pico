'''
Run in vscode terminal to debug circuitpython serial message.
'''

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
serialInstance = serial.Serial()

portList = [str(p) for p in ports]
print(portList)

print("Port No: Port Name")

for portNum, portName in enumerate(portList):
    print(f"{portNum+1}:{portName}")

selection = int(input("Select Port No:"))

selectedPort = portList[selection-1].split(" ")[0]
print(f"You selected:{selectedPort} ")

serialInstance.baudrate = 9600
serialInstance.port = selectedPort
serialInstance.open()

while True:
    if serialInstance.in_waiting:
        msg = serialInstance.readline()
        msg = msg.decode('utf')
        print(msg)
