#coding:utf-8

'''
【程序8】
题目：输出9*9口诀。
1.程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
2.程序源代码
'''

for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            # print str(i)+"*"+ str(j)+"="+str(i*j),
            print ("%d * %d = %-3d" %(j,i,i*j)),
    print ""



# for i in range(1,10):
#     for j in range(1,10):
#         result = i * j

#         print '%d * %d = % -3d' % (i,j,result)
#     print ''
