import os

routerIp = "192.168.2.1" #your router's IP
sites = ["google.com", "facebook.com", "s3.amazonaws.com"] #a list of sites to try

numPingsRouter = "1" #if a single ping fails to your own router then something is wrong
numPingsSites = "3"
intervalSites = "1" #seconds between pings to sites

#here we ping site to see if internet is up
#there are 3 return states, up means we could ping at least one internet site
#down means we could not ping the router, we short circuit in this case as router needs to be restarted immediately
#router means we could ping router, but not internet sites, we allow calling function decide how to handle this

def checkUp():
	#does router serve status page?
	response = os.system("wget -qO- " + routerIp + " 2>&1 >/dev/null")
	if response != 0:
		return "down"

	#if the router is frozen, wget fails faster than ping, so check that first
	#can we ping router?
	response = os.system("ping -c " + numPingsRouter + " " + routerIp + " 2>&1 >/dev/null")
	if response != 0:
		#if we can't even ping router then we are definitely down
		return "down"	

	#try internet sites
	for site in sites:
		response = os.system("ping -c " + numPingsSites + " -i " + intervalSites + " " + site + " 2>&1 >/dev/null")
		if response == 0:
			#if we successfully ping any internet site then we are definitely up
			return "up"

	#if we got here we couldn't ping any site, but could ping router
	return "router"


if __name__ == '__main__':
	print checkUp()