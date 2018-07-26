import motor_functions as mf
import RPi.GPIO as GPIO
import time

mf.setup_motor()

mf.progress(256)

no_mins = 0.25
max_time = 6000*no_mins
print 'ready for control for '+str(no_mins)+' mins.'

i = 0
while i < max_time:
	if GPIO.input(35):
		mf.progress(10)
	i = i+1	
	time.sleep(0.01)

print 'time is up!'
mf.endit()
