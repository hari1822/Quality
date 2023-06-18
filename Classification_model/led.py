import serial
import time
ser =serial.Serial('COM3',9600)

for i in range(3):
    ser.write('1'.encode())
    time.sleep(1)
    print(i)

ser.write('0'.encode())
    
