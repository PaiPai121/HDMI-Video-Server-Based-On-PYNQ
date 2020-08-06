import socket
import keyboard
class SocketServer():
    def __init__(self,host = '127.0.0.1',port = 4000) -> None:
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host,port))
        self.s.listen(1)
    
    def Accept(self):
        conn,addr = self.s.accept()
        with conn:
            print('Connnected by',addr)
            while not keyboard.is_pressed('q'):
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
        self.s.close()

if __name__ == "__main__":
    S=SocketServer()
    S.Accept()