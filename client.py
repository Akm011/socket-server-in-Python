#2019BCSE011 Ashutosh Kumar Maurya
import socket

c = socket.socket()
c.connect(("localhost", 9999))
name = input("Enter your name : ")
c.send(bytes(name, "utf-8"))
print(c.recv(1024).decode())
file = input("Enter the file name you want : ")
c.send(bytes(file, "utf-8"))
print(c.recv(1024).decode())