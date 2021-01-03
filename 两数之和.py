n = list(map(int,input().split(','))) #原组
m = int(input())  #和
p = {}
for i in n:
    p[i] = m - i  #p字典的值为差，键为原组
for i in p:
    if p[i] in p: #i提取的是原组，即差在原组中，即和-原组1=原组2
        print("{:} {:}".format(n.index(i),n.index(p[i]))) #输出下标，分别是原组1的i和原组2的差p[i]
        exit(0)
else:
    print('no answer')
