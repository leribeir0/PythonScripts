#!/usr/bin/python
import socket # Importa o modulo socket

port = 60000 # Reserva a porta 60000 para o servico
s = socket.socket() # Cria o objeto socket
host = socket.gethostname() # Pega o nome da maquina local
s.bind((host,port))
s.listen(5) # Aguarda por uma conexao
print 'Aguardando por uma conexao ...'

while True:
        conn, addr = s.accept() #Estabelece conexao com o cliente
        print 'Conectado a ', addr
        data = conn.recv(1024)
        print('O servidor recebeu ',repr(data))

        filename='arquivo_servidor.txt'
	f = open(filename,'rb')
        l = f.read(1024)
        while(l):
                print ('Enviando: ',repr(l))
                conn.send(l)
                l = f.read(1024)
        f.close()

        print('Envio concluido')
        conn.send('O arquivo foi baixado com sucesso')
        conn.close()
