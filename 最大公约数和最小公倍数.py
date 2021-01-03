m,n = map(int,input().split())
a,b = m,n
i = m % n
while i > 0:
    m,n = n,i
    i = m % n
print(n,int(a*b/n))