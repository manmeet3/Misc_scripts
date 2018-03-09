#!/usr/bin/python

# TCP echo server 
# Created as a reference for testing various utilities and hardware over the network


import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12000)
print ("starting echo server on %s port %s" % server_address)
sock.bind(server_address)
sock.listen(1)

while True:
  print ("waiting for a connection")
  connection, client_address = sock.accept()
  try:
    print ("connection from %s", client_address)
    while True:
      data = connection.recv(16)  # receive 16 bytes
      print ("received -- %s" % data)
      if data:
        print ("echoing")
        connection.sendall(data)
      else:
        print ('no more data from')
		  
  finally:
    connection.close()