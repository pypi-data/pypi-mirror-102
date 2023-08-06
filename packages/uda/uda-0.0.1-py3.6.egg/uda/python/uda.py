import sys

sys.path.append("..")
#!/usr/bin/python3
#coding:utf-8
from proto import uda_pb2
import socket
import struct
import numpy as np

class UDA(object):
    
    def __init__(self, host='127.0.0.1', port=7779):
        self._host = host
        self._port = port
        self._sockfd = -1
        self.connected = False
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.connect();
    def __del__(self):
        self.close()
    
    def connect(self):
        self._sock.connect((self._host, self._port))
        self.connected = True
        
    def close(self):
        self._sock.close()
    
    # 发送数据
    def send_data(self, msgid, data):
        #构造请求头部
        head = struct.pack('ii', msgid, len(data))
        
        #发送数据
        request_data = head + data
        request_len = len(request_data);
        current_len = 0
        
        while current_len < request_len:
            sent = self._sock.send(request_data[current_len:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            current_len += sent
    
    # 接收数据
    def receive_data(self, msgid):
        #接收报头
        head = self._sock.recv(8)
        response_id, response_len = struct.unpack('ii', head)
        
        if response_id == uda_pb2.ID_VERIFY_ERROR:
            if msgid == uda_pb2.ID_LOGIN:
                raise Exception('login failed!')
            raise Exception('access permission exception, please login!')
        
        assert response_id == msgid , 'MessageID error'
        
        #接收数据体
        response_recv = 0
        chunks = []
        
        while response_recv < response_len:
            chunk = self._sock.recv(min(response_len - response_recv, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            response_recv = response_recv + len(chunk)
        
        response_data = b''.join(chunks)
        return response_data
    
    # 获取信号的数据的numpy数组
    def signal(self, tree, path, shot):
        # 构造请求的数据
        sd = uda_pb2.GetSignalDataRequest()
        sd.experiment = tree
        sd.path = path
        sd.shot = shot
        # 序列化数据
        data = sd.SerializeToString();
        # 发送数据
        self.send_data(uda_pb2.ID_SIGNAL_DATA, data)
        # 接收数据
        response_data = self.receive_data(uda_pb2.ID_SIGNAL_DATA)
        # 反序列化数据
        sdr = uda_pb2.GetSignalDataResponse()
        sdr.ParseFromString(response_data)
        return np.frombuffer(sdr.data, dtype=np.float32)   
    
    # 获取信号列表     
    def signal_list(self, tree):
        # 构造请求的数据
        sl = uda_pb2.GetSignalListRequest()
        sl.experiment = tree
        # 序列化数据
        data = sl.SerializeToString()
        # 发送数据
        self.send_data(uda_pb2.ID_SIGNAL_LIST, data)
        # 接收数据
        response_data = self.receive_data(uda_pb2.ID_SIGNAL_LIST)
        # 反序列化数据
        slr = uda_pb2.GetSignalListResponse()
        slr.ParseFromString(response_data)
        return slr  
    
    # 获取信号元数据
    def signal_detail(self, tree, path, shot):
        # 构造请求的数据
        sdl = uda_pb2.GetSignalDetailRequest()
        sdl.experiment = tree
        sdl.path = path
        sdl.shot = shot
        # 序列化数据
        data = sdl.SerializeToString()
        # 发送数据
        self.send_data(uda_pb2.ID_SIGNAL_DETAIL, data)
        # 接收数据
        response_data = self.receive_data(uda_pb2.ID_SIGNAL_DETAIL)
        # 反序列化数据
        sdlr = uda_pb2.GetSignalDetailResponse()
        sdlr.ParseFromString(response_data)
        return sdlr.details[0]  
    
    # 根据起止时刻获取信号数据
    def signal_bytime(self, tree, path, shot, start, end):
        #构造请求的数据
        sdwt = uda_pb2.GetSignalDataByTimeRequest()
        sdwt.experiment = tree
        sdwt.path = path
        sdwt.shot = shot
        sdwt.start = start
        sdwt.end = end
        # 序列化数据
        data = sdwt.SerializeToString()
        # 发送数据
        self.send_data(uda_pb2.ID_SIGNAL_BY_TIME, data)
        # 接收数据
        response_data = self.receive_data(uda_pb2.ID_SIGNAL_BY_TIME)
        # 反序列化数据
        sdwtr = uda_pb2.GetSignalDataByTimeResponse()
        sdwtr.ParseFromString(response_data)
        return np.frombuffer(sdwtr.data, dtype=np.float32)    
        
    # 用户登录    
    def login(self, username, password):
        #构造请求的数据
        self._username = username
        self._password = password
        loginRequest = uda_pb2.LoginRequest()
        loginRequest.username = username
        loginRequest.password = password
        # 序列化数据
        data = loginRequest.SerializeToString();
        # 发送数据
        self.send_data(uda_pb2.ID_LOGIN, data) 
        # 接收数据
        response_data = self.receive_data(uda_pb2.ID_LOGIN)
        # 反序列化数据
        loginResponse = uda_pb2.LoginResponse()
        loginResponse.ParseFromString(response_data)
        self._token=loginResponse.token
        print(self._token)
        
        