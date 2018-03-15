#!/usr/bin/python3
# -*- coding: utf-8 -*-

## Socks Client

import socket
import sys
import time


host = sys.argv[1]
PORT = 5555

for msg in ('Hello', '1', '2', 'abc', 'xyz', 'Bye Bye'):
    sc = socket.socket()
    sc.connect((host, PORT))
    sc.send(msg.encode())
    print(sc.recv(4096).decode())
    sc.close()
    time.sleep(1)

