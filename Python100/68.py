#encoding:utf-8

'''
【程序68】
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
1.程序分析：
2.程序源代码：
'''


from inputs import inputs

a = []
b = []
inputs(a)
m = int(raw_input("yidongweishu:"))
for i in range(len(a)-m,len(a)):
    b.append(a[i])
for i in range(len(a)-m-1,-1,-1):
    a[i+m] = a[i]
for i in range(m):
    a[i] = b[i]
print a
