#encoding:utf-8

'''
【程序12】
题目：判断101-200之间有多少个素数，并输出所有素数。
1.程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，
　　　　　　则表明此数不是素数，反之是素数。 　　　　　　
2.程序源代码：
'''

sum = 0
for i in range(101,201):
    for n in range(2,i/2):
        a = i % n
        if a == 0:
            break
    if a != 0:
        sum += 1
        print i
print sum