#encoding:utf-8

'''
【程序27】
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
1.程序分析：
2.程序源代码：
'''

str = raw_input('请输入若干字符：')

def f(x):
    if x == -1:
        return ''
    else:
        return str[x] + f(x-1)

print(f(len(str)-1))