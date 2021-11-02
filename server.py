
import socket
from os import listdir

def getFiles():  #to send all files with .txt extension
    files = ""
    for i in listdir():
        if i[-3:] == "txt":
            files += i
            files += "\n"
    return files



def getText(fil):       #to resd file data and send to client
    f = open(fil, "r")
    return f.read()


s = socket.socket()
print("Socket Created Successfully")
s.bind(("localhost", 9999))
s.listen(8)
print("Server have started listening successfully")

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print("Connected to", address, "and with the name", name)
    c.send(bytes(getFiles(), "utf-8"))
    print("File names sent successfully")
    name = c.recv(1024).decode()
    print(name)
    c.send(bytes(getText(name), "utf-8"))
    c.close()
    print("Disconnected to", address, "and with the name", name)

