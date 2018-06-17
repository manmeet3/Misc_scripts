#!/usr/bin/python3

''' 
UDP Client

Takes input from stdin and sends it over a UDP socket.
Loops until 'q' entered for quitting.
'''

import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address=('localhost', 12000)
message = 'sample message'  # zybo z7 lwip IP address

try:
  while 1:
    line = input ("Enter a message or q to quit: ")
    if (line == 'q' or line == 'Q'): 
      sys.exit()

    print('Sending: "%s":' % line)
    sent = sock.sendto(str.encode(line),server_address)
	
    data, server = sock.recvfrom(2048)
    print("Recevied: %s" % data) 
	
	
finally:
    print("closing down")
    sock.close()
