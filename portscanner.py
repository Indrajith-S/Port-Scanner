import sys
from datetime import datetime as date
import socket

if len(sys.argv)==2:
    target= socket.gethostbyname(sys.argv[1])
else:
    print("Invalid number of arguements")
    print("Syntax format: python3 portscanner.py <ip>")


print("-"*50)
print("Target: ", target)
print("Time Started: ",date.now())
print("-"*50)

try:
    for port in range(1,100):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result= s.connect_ex((target, port))

        if result==0:
            print(f"Port {port} is open")
        s.close()
    print("-"*50)

except KeyboardInterrupt:
    print("\nExiting Port Scanner")
    sys.close()

except socket.gaierror:
    print("Couldn't resolve hostname")
    sys.close()

except socket.error:
    print("couldn't connect to the server")
    sys.close()
