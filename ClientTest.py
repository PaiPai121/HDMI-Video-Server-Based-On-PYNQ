import socket

import keyboard
class SocketClient():
    def __init__(self,host = '192.168.2.99',port = 4000) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((host,port))
    
    def Send(self):
        self.s.sendall(b'Hello, world')
        data = self.s.recv(1024)
        self.s.close()
        print('Received', repr(data))

if __name__ == "__main__":
    S=SocketClient()
    S.Send()