# -*- coding: utf-8 -*-
"""
Created on Wed May 19 03:33:29 2021

@author: namra
"""

import socket, select
port=12345
sockets=[]
users={}
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
c.bind(('',port))
c.listen(3)
sockets.append(c)

while True:
        ready_to_read,ready_to_write,in_error = select.select(sockets,[],[],0)
        for sock in ready_to_read:
            if sock == c:
                connect, add = c.accept()
                sockets.append(connect)
                print("You are connected from:" + str(add))
            else:
                try:
                    data = sock.recv(1024).decode()
                    if not data:
                        break
                    print("from connected user: "+str(data))
                except:
                        continue
c.close()
