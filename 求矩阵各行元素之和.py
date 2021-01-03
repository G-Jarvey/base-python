m,n = map(int,input().split())
mat=[]
for i in range(m):
    s = input()
    mat.append([int(n) for n in s.split()])
for j in range(m):
    sum = 0
    for k in range(n):
        sum += mat[j][k]
    print(sum)