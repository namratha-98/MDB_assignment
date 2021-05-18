# -*- coding: utf-8 -*-
"""
Created on Wed May 19 03:34:18 2021

@author: namra
"""

import socket
c=socket.socket()
port=12345
c.connect(('127.0.0.1', port))

message=input("-> ")
while True:
    if message == 'exit':
        break;
    else:
        c.send(message.encode())
    message = input("-> ")
c.close()