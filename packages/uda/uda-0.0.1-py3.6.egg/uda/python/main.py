#!/usr/bin/python3
#coding:utf-8

import sys
sys.path.append("..")

from python.uda import UDA
import json

from google.protobuf.json_format import MessageToJson
from google.protobuf.json_format import MessageToDict

if __name__ == "__main__":
    uda = UDA("202.127.205.63", 7778)
    
    print("===================Signal Data=====================")
    ret = uda.signal('east', 'T1:IPM', 96914)
    print(ret)
    print("===================================================")
    print("===================Signal List=====================")
    ret = uda.signal_list('east')
    arr = MessageToJson(ret)
    print(ret.item[0])
    print("===================================================")
    
    print("===================Signal Detail===================")
    ret = uda.signal_detail('east', 'T1::IPM', 96914)
    print(ret)
    
    print("===================Signal Data=====================")
    ret = uda.signal_bytime('east', 'T1:IPM', 96914, 0.5, 0.501)
    print(ret)
    
    uda.login("uda", "123")
    