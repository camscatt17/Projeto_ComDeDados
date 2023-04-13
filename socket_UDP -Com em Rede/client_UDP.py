#!/usr/bin/python3

import socket

ip_server = '192.168.0.162'
port_server= 5000
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

destino = (ip_server, port_server)

msg = input()

udp.sendto(msg.encode('utf-8'), destino)

udp.close()