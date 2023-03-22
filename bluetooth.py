import socket
import picar_4wd as fc
import sys
import tty
import termios
import asyncio
import time
from bluedot.btcomm import BluetoothServer
from signal import pause
from picar_4wd.utils import *

speed = 30

def data_received(data):

	if "forward" in data:

		fc.forward(speed)
		x = 0
		for i in range(1):
			time.sleep(0.5)
			x += speed * 0.5
		print("%smm"%x)
		fc.stop()
		
	elif "left" in data:

		fc.turn_left(speed)
		x = 0
		for i in range(1):
			time.sleep(0.5)
			x += speed * 0.5
		print("%smm"%x)

		fc.stop()
		
	elif "right" in data:
		
		fc.turn_right(speed)
		x = 0
		for i in range(1):
			time.sleep(0.5)
			x += speed * 0.5
		print("%smm"%x)
		fc.stop()
		
	elif "backward" in data:
		
		fc.backward(speed)
		x = 0
		for i in range(1):
			time.sleep(0.5)
			x += speed * 0.5
		print("%smm"%x)
		fc.stop()

	print(data)
	s.send(data)
	
s = BluetoothServer(data_received)
pause()
