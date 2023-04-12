#!/usr/bin/env python3
#Exemplo de uma conexão local entre cliente e servidor

#Script que funcionará como servidor

import socket #Primeira coisa ser fazer: importar o módulo socket

#Cria-se duas constantes uma vez que o endereço de um socket é composto pela combinação de um endereço IP com o n° de porta
HOST = 'localhost'
PORT = 50000

#Cria-se um socket que recebe endereços IPv4 (parâmetro socket.AF_INET) e utiliza protocolo de transporte TCP (socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST, PORT)) #O socket precisa ter os valores de host e porta vinculados, sendo este processo feito através do método bind

s.listen() #O módulo de socket fica no modo de escuta
print('Aguardando conexão de um cliente')

conn, ender = s.accept() #Deve-se aceitar a conexão quando ela chegar

print('Conectado em {}'.format(ender)) #Mensagem que indica que a conexão foi aceita


while True:
    data = conn.recv(1024) #As mensagens podem ter tamanhos variádos, contudo, neste exemplo determina-se o tamanho de até 1024 bytes
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)