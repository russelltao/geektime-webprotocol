#! /usr/bin/python
# -*- coding: utf-8 -*-
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ("127.0.0.1",12345)
sock.bind(server_address)
sock.listen(100)

while True:
    conn,client_address = sock.accept()
    try:
        data = conn.recv(4096)
        response = 'HTTP/1.1 200 OK\r\nContent-Disposition: attachment; filename=“aaa.jpg”\r\nContent-Length: 10\r\n\r\nHelloWorld'
        conn.send(response.encode())
    finally:
        conn.close()
