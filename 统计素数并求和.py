m,n = map(int,input().split())
count = 0
sum = 0
sign = 1
for i in range(m,n+1):
    if i != 1:
        for x in range(2,i):
            if i%x == 0:
                sign = 0
        if sign != 0:
            sum = sum + i
            count += 1
        sign = 1
print(count,sum)
                
        