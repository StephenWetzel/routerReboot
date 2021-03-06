import time
import RPi.GPIO as io

power_off_time = 10 #time to stay off, in seconds

io.setmode(io.BCM)
power_pin = 23
io.setup(power_pin, io.OUT)

def powerOn():
	io.output(power_pin, True)
	print("POWER ON")

def powerOff():
	io.output(power_pin, False)
	print("POWER OFF")

def powerCycle():
	powerOff()
	time.sleep(power_off_time)
	powerOn()

if __name__ == '__main__':
	powerCycle()