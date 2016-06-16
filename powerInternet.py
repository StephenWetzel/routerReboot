import checkInternet
import powerCycle
import time
import datetime

sleepSuccess = 30 #seconds to wait after we test internet again if it was up
sleepFail = 600 #seconds to wait after internet was down, and we power cycle

powerCycle.powerOn()
time.sleep(100)

while True:
	if checkInternet.checkUp():
		print str(datetime.datetime.now()) + " Internet works"
		time.sleep(sleepSuccess)
	else:
		print str(datetime.datetime.now()) + " Internet down"
		powerCycle.powerCycle()
		time.sleep(sleepFail)
