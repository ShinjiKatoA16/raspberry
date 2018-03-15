#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import time

sc = socket.socket()

PORT = 5555
MAX_Q = 5
#hostname = socket.gethostname()
#print('Host Name:', hostname)
sc.bind(('', PORT))

print('Listening')
sc.listen(MAX_Q)

while True:
    client, addr = sc.accept()
    print('Receiving from', addr)
    in_text = client.recv(4096).decode()
    print(in_text)
    client.send((in_text + ' OK').encode())
    client.close()
sc.close()
