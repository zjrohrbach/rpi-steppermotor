global GPIO
global time
import RPi.GPIO as GPIO
import time

def setup_motor():
	GPIO.setmode(GPIO.BOARD)

	global ControlPin
	global seq

	ControlPin = [7,11,13,15]

	for pin in ControlPin:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,0)

	seq =	[	[1,0,0,0],
			[1,1,0,0],
			[0,1,0,0],
			[0,1,1,0],
			[0,0,1,0],
			[0,0,1,1],
			[0,0,0,1],
			[1,0,0,1]	]
	
	global switch_in
	global switch_out

	switch_in = 35
	switch_out = 37

	GPIO.setup(switch_out,GPIO.OUT)
	GPIO.setup(switch_in,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
	GPIO.output(switch_out,1)

def progress(steps):
	for i in range(steps):
		for halfstep in range(8):
			for pin in range(4):
				GPIO.output(ControlPin[pin],seq[halfstep][pin])
			time.sleep(0.001)

	for pin in range(4):
		GPIO.output(ControlPin[pin],0)
def endit():
	GPIO.cleanup()
