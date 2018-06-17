#!/usr/bin/python

'''
TCP client 

Takes input from stdin and sends it over a TCP socket.
Loops until 'q' entered for quitting.
'''

import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12000)
print ("connecting to %s port %s" % server_address)
sock.connect(server_address)

try:
  while 1:
    line = input ("Enter a message or q to quit: ")
    if (line == 'q' or line == 'Q'): 
      sys.exit()
    sock.sendall(str.encode(line))
    amount_received = 0
    amount_expected = len(line)
	
    while amount_received < amount_expected:
      data = sock.recv(16)
      amount_received += len(data)
      print ("Received: %s" % data )
	  
finally:
  print ("closing socket")
  sock.close()
