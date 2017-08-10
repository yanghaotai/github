#coding:utf-8

'''
【程序3】
题目：一个整数，它加上100后是一个完全平方数，再加上268又是一个完全平方数，请问该数是多少？
1.程序分析：完全平方数，平方根后为整数(10以内)
2.程序源代码：
'''

import math
for i in range(100000):
    if ((math.sqrt(i+100)%1 == 0)&(math.sqrt(i+268)%1 == 0)):
        print i
        # print math.sqrt(i+100),math.sqrt(i+100+268)

# import math
# for i in range(10000):
#     #转化为整型值
#     x = int(math.sqrt(i + 100))
#     y = int(math.sqrt(i + 268))
#     if(x * x == i + 100) and (y * y == i + 268):
#         print i

