#!/usr/bin/python

# UDP test utility for use with Digilent Zybo z7-20 running lwip

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address=('172.0.1.10', 7)
message = 'sample message'  # zybo z7 lwip IP address

try:
    print('Sending: "%s":' % message)
    sent = sock.sendto(str.encode(message),server_address)
	
    print("waiting for response...")
    data, server = sock.recvfrom(2048)
    print("Recevied: %s" % data) 
	
	
finally:
    print("closing down")
    sock.close()