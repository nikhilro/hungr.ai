import socket
import struct
from time import sleep

motor_num = struct.pack('????', 0,1,0,0)
motor_num2 = struct.pack('????', 1,0,1,0)
motor_num3 = struct.pack('????', 1,1,1,0)
print (motor_num)
print (motor_num2)
print (motor_num3)

TCP_IP = '0.0.0.0'
TCP_PORT = 25565
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    conn.send(motor_num)  # echo
    sleep(0.8)
    conn.send(motor_num2)
    sleep(0.8)
    conn.send(motor_num3)

