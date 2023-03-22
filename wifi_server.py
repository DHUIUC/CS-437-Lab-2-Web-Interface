import socket
import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import time
from picar_4wd.speed import Speed
from picar_4wd.utils import *


HOST = "192.168.1.3" # IP address of your Raspberry PI
PORT = 65432          # Port to listen on (non-privileged ports are > 1023)
speed = 30
distance = 0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    try:
        while 1:
            client, clientInfo = s.accept()
            print("server recv from: ", clientInfo)
            data = client.recv(1024)      # receive 1024 Bytes of message in binary format
            if data != b"":
                print(data)
                stringData = data.decode('utf-8')
                print(stringData)
                #if "forward" in stringData or "left" in stringData or "right" in stringData or "plus" in stringData:
                #    moveCar(stringData)
                
                if "forward" in stringData:

                    fc.forward(speed)
                    x = 0
                    for i in range(1):
                        time.sleep(0.5)
                        x += speed * 0.5
                    print("%smm"%x)
                    fc.stop()
                    
                elif "left" in stringData:

                    fc.turn_left(speed)
                    x = 0
                    for i in range(1):
                        time.sleep(0.5)
                        x += speed * 0.5
                    print("%smm"%x)

                    fc.stop()
                    
                elif "right" in stringData:
                    
                    fc.turn_right(speed)
                    x = 0
                    for i in range(1):
                        time.sleep(0.5)
                        x += speed * 0.5
                    print("%smm"%x)
                    fc.stop()
                    
                elif "backward" in stringData:
                    
                    fc.backward(speed)
                    x = 0
                    for i in range(1):
                        time.sleep(0.5)
                        x += speed * 0.5
                    print("%smm"%x)
                    fc.stop()
                    
                elif "plus" in stringData:
                    if speed < 50:
                        speed = speed + 10
                        print(speed)
                    sendData = bytes(str(speed).encode('utf-8'))
                    data = sendData
                    
                elif "minus" in stringData:
                    if speed > 10:
                        speed = speed - 10
                    sendData = bytes(str(speed).encode('utf-8'))
                    data = sendData
                    
                elif "temp" in stringData:
                    temp = cpu_temperature()
                    sendData = bytes(str(temp).encode('utf-8'))
                    data = sendData
                elif "battery" in stringData:
                    battery = power_read()
                    sendData = bytes(str(battery).encode('utf-8'))
                    data = sendData
                
                client.sendall(data) # Echo back to client
    except Exception as e: 
        print(e)
        print("Closing socket")
        client.close()
        s.close()
    
    finally:
        fc.stop()
    
    

