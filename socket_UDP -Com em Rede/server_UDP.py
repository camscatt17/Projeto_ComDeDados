#!/usr/bin/python3

import socket
host = ''
port = 5000

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = (host, port)
udp.bind(server)

msg, adr_client = udp.recvfrom(1024)
msg = msg.decode('utf-8')
print("Recebi ", msg, " do cliente ", adr_client)

udp.close()
