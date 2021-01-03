import math
sign = 0
m,n = map(int,input().split())
for i in range (m,n+1):
    s = [1]
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            s.append(j)
            s.append(int(i/j))
    if sum(s) == i:
        sign = 1
        s.sort()
        s = map(str,s)
        print('{:d} = {}'.format(i,' + '.join(s)))
if sign == 0:
    print('None')