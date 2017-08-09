#encoding:utf-8

import urllib.request
from html.parser import HTMLParser
from html.entities import name2codepoint
import re
import xlrd
import xlwt3

sock = urllib.request.urlopen(r"http://www.qunar.com/routes/beijing_city/beijing_city-haerbin.htm")
htmlSource = str(sock.read().decode('utf-8'))
sock.close()
wb = xlwt3.Workbook()
sheet = wb.add_sheet('sheet 1')
sheet.write(0,0,'始发点')
sheet.write(0,1,'终点')
sheet.write(0,2,r'里程/km')
sheet.write(0,3,r'价格/元')
list_data = []
class MyHtmlParser(HTMLParser):
    
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        global row
    def handle_starttag(self,tag,attrs):
        if tag == "p":
            if len(attrs) == 0:pass
            else:
                for (key,value) in attrs:
                    if key == "style" and value == "text-indent:0;line-height:18px;":
                        self.flag = 1

    def handle_endtag(self,tag):
        if tag == "a":
            if self.flag == 1:
                self.flag = 2
            
    def handle_data(self,data):
        if self.flag == 2:
            print(data)
            info = re.search(r"(\w{2,4})到(\w{2,4})整个飞行里程(\d{3,5})KM，全价(\d{3,5})元",data)
            list_data.append([info.group(1),info.group(2),info.group(3),info.group(4)])
            self.flag = 0
            
parser = MyHtmlParser()
parser.feed(htmlSource)


