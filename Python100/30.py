#encoding:utf-8

'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　　　
1.程序分析：同29例
2.程序源代码：
'''

x = int(raw_input("input a number:\n"))
a = x / 10000
b = x / 10000 % 1000
c = x % 100 / 10
d = x % 10
if (a == d)&(b ==c):
    print "%d is huiwen" % x
else:
    print "%d is not huiwen" % x


