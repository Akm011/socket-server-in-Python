import socket


def read_till_newline(sock):
    message = b""
    while True:
        char = sock.recv(1)
        if char == b'\n':
            break
        message += char
    return message.decode()


s = socket.socket()
host = 'localhost'
port = 9990

s.bind((host, port))
s.listen()
print("Ready to connect ")

while True:
    c,*_ = s.accept()
    while True:
        msg = input("> ") + "\n"
        c.send(msg.encode())
        incoming = read_till_newline(c)
        if incoming:
            print(incoming)