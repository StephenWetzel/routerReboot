import os

routerIp = "192.168.2.1" #your router's IP
sites = ["8.8.8.8", "google.com", "facebook.com"] #a list of sites to try

numPingsRouter = "1" #if a single ping fails to your own router then something is wrong
numPingsSites = "3"

def checkUp():
	response = os.system("ping -c " + numPingsRouter + " " + routerIp + " 2>&1 >/dev/null")
	#print response
	if response != 0:
		#if we can't even ping router then we are definitely down
		return False

	for site in sites:
		response = os.system("ping -c " + numPingsSites + " " + site + " 2>&1 >/dev/null")
		if response == 0:
			#if we successfully ping any internet site then we are definitely up
			return True

	#if we got here we couldn't ping any site
	return False
