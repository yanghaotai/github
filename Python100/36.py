#encoding:utf-8

'''
【程序36】
题目：求100之内的素数　　　
1.程序分析：质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数。
2.程序源代码：
'''

# for n in range(2,101):
#     flag = 1
#     for m in range(2,n):
#         if n % m == 0:
#             flag = 0
#             break
#     if flag == 1:
#         print n,


# from math import sqrt
# if __name__ == '__main__':
#     N = 100
#     a = range(0,N)
#     for i in range(2,int(sqrt(N))):
#         for j in range(i + 1,N):
#             if (a[i] != 0) and (a[j] != 0):
#                 if a[j] % a[i] == 0:
#                     a[j] = 0
#     print
#     for i in range(2,N):
#         if a[i] != 0:
#             print "%5d" % a[i]
#             if (i - 2) % 10 == 0:
#                 print


from math import sqrt
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(2,100):
    if is_prime(i):
        print i