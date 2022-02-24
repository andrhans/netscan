import pyfiglet
import sys
import socket
from datetime import datetime
from time import sleep

welcome_banner=pyfiglet.figlet_format("Port Scanner")
print(welcome_banner)

if len(sys.argv) == 2:
    target=socket.gethostbyname(sys.argv[1])
else:
    print("Missing argument! Did you forget the IP address? \n\nTry again adding the IP address of the desired host")
    sys.exit()

print("*" * 50)
print("Scan started...")
print("Start time: " + str(datetime.now()))
print("Scanning host: " +target)
print("*" * 50)

try:
    for port in range(1,1000):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(10)

        result=s.connect_ex((target, port))
        if result == 0:
            print("Port {} open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nStopping scan...")
    sleep(5)
    print("\nScan terminated")
    sys.exit()

except socket.gaierror:
    print("\nUnresolved hostname...")
    sys.exit()

except socket.error:
    print("\nSpecified host not responding...")
    sys.exit()

