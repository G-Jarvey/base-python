def fib(n):
    if(n==0)or(n==1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
def PrintFN(m,n):
    lis = []
    for i in range(25):
        if m <= int(fib(i)) <= n:
            lis.append(fib(i))
    return lis