#encoding:utf-8

'''
程序31】
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续
　　　判断第二个字母。
1.程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。
2.程序源代码：
星期一： Mon.=Monday
星期二： Tues.=Tuesday
星期三： Wed.=Wednesday
星期四： Thur.=Thursday
星期五： Fri.=Friday
星期六： Sat.=Saturday
星期天： Sun.=Sunday
'''
# s1 = raw_input("input first num:\n")
# a = ["M","m","T","t","W","w","F","f","S","s"]
# b = ["U","u","H","h"]
# c = ["A","a","U","u"]
# if s1 in a:
#     if s1 in ["M","m"]:
#         print "Today is Monday!"
#     elif s1 in ["W","w"]:
#         print "Today is Wednesday!"
#     elif s1 in ["F","f"]:
#         print "Today is Friday!"
#     elif s1 in ["T","t"]:
#         s2 = raw_input("input second num:\n")
#         if s2 in b:
#             if s2 in ["U","u"]:
#                 print "Today is Tuesday!"
#             else:
#                 print "Today is Thursday!"
#         else:
#             print "second num is error"
#     elif s1 in ["S","s"]:
#         s2 = raw_input("input second num:\n")
#         if s2 in c:
#             if s2 in ["U","u"]:
#                 print "Today is Sunday!"
#             else:
#                 print "Today is Saturday!"
#         else:
#             print "second num is error"
# else:
#     print "first num is error"



# from sys import stdin
# letter = stdin.read(1)
# stdin.flush()
# while letter  != 'Y':
#     if letter == 'S':
#         print 'please input second letter'
#         letter = stdin.read(1)
#         stdin.flush()
#         if letter == 'a':
#             print 'Saturday'
#         elif letter  == 'u':
#             print 'Sunday'
#         else:
#             print 'data error'
#             break
#     elif letter == 'F':
#         print 'Friday'
#         break
#     elif letter == 'M':
#         print 'Monday'
#         #break
#     elif letter == 'T':
#         print 'please input second letter'
#         letter = stdin.read(1)
#         stdin.flush()
#         if letter  == 'u':
#             print 'Tuesday'
#         elif letter  == 'h':
#             print 'Thursday'
#         else:
#             print 'data error'
#             break
#     elif letter == 'W':
#         print 'Wednesday'
#     else:
#         print 'data error'
#     letter = stdin.read(1)
#     stdin.flush()


s1 = raw_input("input first num:\n")
while s1 != '':
    if s1 in ["M","m"]:
        print "Today is Monday!"
        break
    elif s1 in ["W","w"]:
        print "Today is Wednesday!"
        break
    elif s1 in ["F","f"]:
        print "Today is Friday!"
        break
    elif s1 in ["T","t"]:
        s2 = raw_input("input second num:\n")
        while s2 != '':
            if s2 in ["U","u"]:
                print "Today is Tuesday!"
                break
            elif s2 in ["H","h"]:
                print "Today is Thursday!"
                break
            else:
                print "second num is error"
                s2 = raw_input("input second num:\n")
        break
    elif s1 in ["S","s"]:
        s2 = raw_input("input second num:\n")
        if s2 != '':
            if s2 in ["U","u"]:
                print "Today is Sunday!"
                break
            elif s2 in ["A","a"]:
                print "Today is Saturday!"
                break
            else:
                print "second num is error"
                s2 = raw_input("input second num:\n")
        break
    else:
        print "first num is error"
        s1 = raw_input("input first num:\n")