Use a Raspberry Pi to reboot my router when it crashes

# checkInternet.py
checkInternet.py returns True if it can successfully ping a site, False otherwise.

# powerCycle.py
powerCycle.py provides functions to power the router off and on, and a power cycle function.  It does this using a 120 V relay [Powerswitch tail 2](https://www.adafruit.com/product/268).  The wiring is as simple as it gets, just pin 23 to terminal 1 on the relay, and the ground to terminal 2.  The relay is normally open, and needs to be pulled high to close.  The pin on the Pi starts low, in the future I'd like to see if some pins start high reliably.  Failing that I could add a pull up resistor.

# powerInternet.py
powerInternet.py just ties everything together.  It loops forever, checking the internet, and when it fails it'll do a power cycle then sleep for 10 mins.