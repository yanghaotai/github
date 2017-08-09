#encoding:utf-8

# for i in range(100000):
#     print "6217000****03"+str(i).zfill(6)

f = open('C:/Users/Administrator/Desktop/1.txt','w')
for i in range(20000):
    n = "6217000****03"+str(i).zfill(6)
    f.write(n+"\n")
f.close()