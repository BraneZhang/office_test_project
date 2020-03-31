#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import socket

# def check_port(host, port):
#     """检测指定的端口是否被占用"""
#
#     #创建socket对象
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     try:
#         s.connect((host, port))
#         s.shutdown(2)
#     except OSError as msg:
#         print('port %s already be in use !' % port)
#         print(msg)
#         return False
#     else:
#         print('port %s is available! ' % port)
#         return True

def check_port(port):
    """检测指定端口是否被占用"""
    # 查找对应端口的pid
    cmd_find = 'netstat -aon | findstr %s' % port
    result = os.popen(cmd_find).read()
    # print(cmd_find)
    if not result:
        print('port %s is available! ' % port)
        return True
    else:
        print('port %s already be in use !' % port)
        return False

def release_port(port):
    """释放指定的端口"""

    #查找对应端口的pid
    cmd_find='netstat -aon | findstr %s' %port
    print(cmd_find)

    #返回命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)

    if  str(port) and 'LISTENING' in result:
        #获取端口对应的pid进程
        i=result.index('LISTENING')
        start=i+len('LISTENING')+7
        end=result.index('\n')
        pid=result[start:end]

        # 关闭被占用端口的pid
        cmd_kill='taskkill -f -pid %s' %pid
        print(cmd_kill)
        os.popen(cmd_kill)

    else:
        print('port %s is available !' %port)

if __name__ == '__main__':
    host='127.0.0.1'
    port=4723
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((host,port))
    # s.shutdown(2)
    cmd_find = 'netstat -aon | findstr 4723'
    result = os.popen(cmd_find).read()
    print(result)
    if not result:
        print('port is available')
    else:
        print('port in use')

# check_port(host,port)
    # release_port(port)