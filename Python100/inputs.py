#encoding:utf-8

def inputs(a):
    num = int(raw_input("input N number:"))
    for i in range(num):
        print "num" + str(i+1) + ":"
        n = int(raw_input(""))
        a.append(n)
    print a



