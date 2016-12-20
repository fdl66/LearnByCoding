#!/usr/bin/env python
# coding:utf-8
import socket
from multiprocessing.dummy import Pool as ThreadPool

def scan(port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.5)
    if client.connect_ex(("123.249.94.160", port)) == 0:
        print("Port: {0} is open".format(port))
    client.close()

if __name__ == "__main__":
    pool = ThreadPool(50)
    pool.map(scan, range(1, 65535))
    pool.close()
    pool.join()
