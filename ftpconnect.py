#!/usr/bin/python

import socket

ip = raw_input("Digite o ip: ")
porta = input("Digite a porta: ")

meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if meusocket.connect_ex((ip,porta)):
	print "Erro ao estabelecer conexao. Tente novamente"
else:
	print meusocket.recv(1024)

