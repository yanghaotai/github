#encoding:utf-8

'''
【程序69】
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出
　　　圈子，问最后留下的是原来第几号的那位。
1. 程序分析：
2.程序源代码：
'''
# # def num(n):
# #     for i range(n):
#
# a = []
# for i in range(1,101):
#     a.append(i)
# print a
#
# for i in range(len(a)-1,-1,-1):
#     # print a[i],
#     if a[i] % 3 == 0:
#         a.pop(i)
#         print a
# # print a
# print len(a)
#
# for i in range(len(a)-1,-1,-1):
#     # print a[i],
#     if (i+1) % 3 == 0:
#         a.pop(i)
#         print a
# # print a


if __name__ == '__main__':
    nmax = 50
    n = int(raw_input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0 : k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n : i = 0

    i = 0
    while num[i] == 0: i += 1
    print num[i]