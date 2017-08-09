#encoding:utf-8

'''
【程序39】
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
1. 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后
　　　　　此元素之后的数，依次后移一个位置。
2.程序源代码：
'''

a = []
num = int(raw_input("input N number:"))
for i in range(num):
    print "num" + str(i+1) + ":"
    n = int(raw_input(""))
    a.append(n)
a.sort()
print a
nu = int(raw_input("insert number:"))
if nu > a[len(a) - 1]:
    a.append(nu)
else:
    for i in range(len(a)):
        if a[i] > nu:
            a.insert(i, nu)
print a

