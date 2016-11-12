#!/usr/bin/env python
# coding:utf-8
import sys
import requests
from bs4 import BeautifulSoup

class Parser(object):
    def __init__(self, ip):
        self.ip = ip
        self.ip138_url = "http://www.ip138.com/"
        self.ipcn_url = "http://ip.cn/index.php"
        self.headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.87 Safari/537.36"}


    def ip138(self):
        resp = requests.get("{0}ips1388.asp?ip={1}&action=2".format(self.ip138_url, self.ip), headers=self.headers)
        soup = BeautifulSoup(resp.content, "lxml")
        table = soup.find_all("table")[2]
        tr = table.find_all("tr")[2]
        li = tr.find_all("li")
        for i in li:
            print i.string

    def ipcn(self):
        resp = requests.get("{0}?ip={1}".format(self.ipcn_url, self.ip), headers=self.headers)
        soup = BeautifulSoup(resp.content, "lxml")
        result = soup.find_all(class_ = "well")[0].find_all("p")
        for i in result:
            print i.text

    def main(self):
        print "**" * 10 + "ip138" + "**" * 10
        self.ip138()
        print "**" * 10 + "ip.cn" + "**" * 10
        self.ipcn()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        p = Parser(sys.argv[1])
        p.main()
    else:
        print "python ip.py 8.8.8.8"