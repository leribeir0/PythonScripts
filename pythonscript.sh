#!/usr/bin/python
import socket
ip = raw_input ("Informe o ip: ")
port = input ("Informe a porta: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if s.connect_ex((ip,port)):
	print "Port", port, "is closed"
else:
	print "Port", port, "is open"
