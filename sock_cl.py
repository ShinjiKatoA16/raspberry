#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Socks Client

import socket
import sys
import time

host = sys.argv[1]
PORT = 5555

for i in range(100):
    msg = str(i)
    sc = socket.socket()
    sc.connect((host, PORT))
    sc.send(msg.encode())
    print(sc.recv(4096).decode())
    time.sleep(1)
    sc.close()
