import serial

ser = serial.Serial('/dev/ttyACM0',38400)
while True:
    read_serial=ser.readline().decode().strip()
    print(read_serial)
