#!/usr/bin/python
import socket
ip_alvo = raw_input("Digite o ip do alvo: ")
for porta in range(1,65535):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if s.connect_ex((ip_alvo,porta)) == 0:
		print "Porta ",porta," aberta"
		s.close()

