import socket
import threading
import struct
import cv2
import numpy

class SocketServer:
    '''进行SocketServer的初始化配置'''
    def __init__(self,addr="",port = 8880) -> None:
        self.resolution = (1920,1080) # 分辨率
        self.img_fps = 30 # 帧率
        self.Set_Socket(addr,port) # 调用设置Socket的方法

    def Set_Socket(self,addr,port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) ## 允许端口复用
        self.server.bind((addr,port))
        self.server.listen(5) # 允许连接数量
        print("addr:",addr,"port:",port)

def check(server,client):
    info = struct.unpack('lhh',client.recv(8))

    if info[0] > 888:
        server.img_fps = int(info[0]) - 888
        server.resolution = list(server.resolution)
        server.resolution[0] = info[1]
        server.resolution[1] = info[2]
        server.resolution = tuple(server.resolution) ## 修正分辨率
        return 1
    else:
        return 0

def RealTime_Image(hdmi_in,server,client,D_addr):
    if (check(server,client) == 0):
        return
    img_param =[int(cv2.IMWRITE_JPEG_QUALITY),server.img_fps]
    while(1):
        # 读取一帧视频
        server.img = hdmi_in.readframe()
        server.img = cv2.resize(server.img, server.resolution)# 按格式生成图片
        img_encode = cv2.imencode('.jpg',server.img,img_param)
        img_code = numpy.array(img_encode[1])
        server.img_data = img_code.tostring()
        client.send(
            struct.pack("lhh",len(server.img_data),server.resolution[0],server.resolution[1]) + server.img_data)

if __name__ == "__main__":
    S = SocketServer()
    while(1):
        client,D_addr = S.server.accept()
        clientThread = threading.Thread(None,target = RealTime_Image,args = (S,client,D_addr,))
        clientThread.start()