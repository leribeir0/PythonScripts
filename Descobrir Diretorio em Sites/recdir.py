#!/usr/bin/python

import sys,requests

if len(sys.argv) == 1:
	print "Exemplo de uso :" + sys.argv[0] + "http://meusite.com.br worlist.txt"
else:
	arq = open (sys.argv[2],"r")
	for linha in arq:
		r = requests.get("%s/%s/" % (sys.argv[1],linha.strip()))
		if (r.status_code  == 200):
			print "Diretorio encontrado: " + linha
