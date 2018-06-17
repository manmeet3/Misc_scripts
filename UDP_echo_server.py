#!/usr/bin/python

'''
UDP Echo Server

Echoes back the data to the sending UDP client.
Exits on receiving an empty packet.
'''

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 12000)
print ("Starting UDP echo server on %s and port %s" % server_address)
sock.bind(server_address)

while True:
    payload, client_address = sock.recvfrom(1024)
    if payload:
        print (payload)
        print ("Echoing data back to " + str(client_address))
        sent = sock.sendto(payload, client_address)
    else:
        print ("Connection closed by %s", str(client_address))
        sys.exit()

