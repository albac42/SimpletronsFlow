import serial.tools.list_ports
#Print Initial Serial Ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)
    
serial = serial.tools.list_ports.comports()