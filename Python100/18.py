#encoding:utf-8

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时
　　　共有5个数相加)，几个数相加有键盘控制。
1.程序分析：关键是计算出每一项的值。
2.程序源代码：
'''

a = int(raw_input("a=:"))
b = int(raw_input("b=:"))
sum1 = 0
sum2 = 0
for i in range(b):
    sum1 += a * 10 ** i
    sum2 += sum1
print sum2



# Tn = 0
# Sn = []
# n = int(raw_input('n = :\n'))
# a = int(raw_input('a = :\n'))
# for count in range(n):
#     Tn = Tn + a
#     a = a * 10
#     Sn.append(Tn)
#     print Tn
#
# Sn = reduce(lambda x,y : x + y,Sn)
# print Sn
