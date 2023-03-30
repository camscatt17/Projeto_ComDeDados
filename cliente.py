#!/usr/bin/env python3
#Script que funcionará como Cliente

import socket

HOST = '127.0.0.1'
PORT = 50000 #A porta deve ser a mesma que a do servidor para que eles existir a conexão

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(str.encode('Boa noite Camis!'))
data = s.recv(1024) #Recebe os dados até um tamanho especificado

print('Mensagem ecoada:', data.decode())
