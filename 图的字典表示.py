n = int(input())
side = 0
length = 0
for i in range(n):
    s = eval(input())  #接收一个顶点的所有属性s
    for key1 in s:       #key1为s的键，即起始顶点
        value1 = s[key1]   #value为key1后的值
        for key2 in value1: #key2为第二层键，即起始顶点所连顶点
            length += value1[key2] #key2的值即为边长length
            side += 1 #key2,即所连顶点数就等于连接的边数
print("{:d} {:d} {:d}".format(n,side,length))
        
    