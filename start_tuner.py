#!/usr/bin/python
import os
#os.system("/usr/local/bin/onkyo -n 414 volume=25 >> cronlog")

os.system("/usr/local/bin/onkyo --host 192.168.1.2 PWR01")
os.system("/usr/local/bin/onkyo --host 192.168.1.2 SLI24")
#os.system("date >> /home/pi/cronlog")
os.system("/usr/local/bin/onkyo --host 192.168.1.2 volume=30 >> cronlog")

#import eiscp
# Create a receiver object, connecting to the host
#receiver = eiscp.eISCP('192.168.1.2')
# Turn the receiver on, select PC input
#receiver.command('power on')
#receiver.command('volume 5' )
#receiver.command('source pc')
#receiver.raw('SLI26')
#receiver.disconnect()
#192.168.1.2
#onkyo -n 414 power=on
#onkyo -n 414 SLI26 volume=28
