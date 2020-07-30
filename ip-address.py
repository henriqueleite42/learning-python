# Inspired in https://www.instagram.com/p/CDMT53XgDV8/

import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + ip_address)
