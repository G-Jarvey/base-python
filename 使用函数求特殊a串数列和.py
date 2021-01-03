def fn(a,n):
    sum = 0
    b = 0
    for i in range(n):
        b = b + a
        a = a*10
        sum = sum + b
    return sum
print(fn(2,3))
            
