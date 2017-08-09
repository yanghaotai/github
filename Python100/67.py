#encoding:utf-8

'''
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
1.程序分析：谭浩强的书中答案有问题。　　　　　　
2.程序源代码：
'''

from inputs import inputs

a = []
inputs(a)
max = a[0]
min = a[len(a)-1]
for n in range(1,len(a)-1):
    if a[n] > max:
        max = a[n]
        flagmax = n
    if a[n] < min:
        min = a[n]
        flagmin = n
if a[0] != max:
    a[0],a[flagmax] = a[flagmax],a[0]
if a[len(a)-1] != min:
    a[len(a)-1],a[flagmin] = a[flagmin],a[len(a)-1]
print a


# def inp(numbers):
#     for i in range(5):
#         numbers.append(int(raw_input('input a number:\n')))
#     # numbers.append(int(raw_input('input a number:\n')))
#
# nums = []
# inp(nums)
# print nums