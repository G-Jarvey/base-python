s = list(map(int,input().split(',')))
lis = [i for i in range(6,11) if i not in s]
for x in lis:
    print(x, end=' ' if x != lis[-1] else '')
