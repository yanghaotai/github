#encoding:utf-8

'''
【程序40】
题目：将一个数组逆序输出。
1.程序分析：用第一个与最后一个交换。
2.程序源代码：
'''
a = []
num = int(raw_input("input N number:"))
for i in range(num):
    print "num" + str(i+1) + ":"
    n = int(raw_input(""))
    a.append(n)
print a
for i in range(len(a),0,-1):
    print a[i-1]