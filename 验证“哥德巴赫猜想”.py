import math
def isprime(n):
    isprime = True
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            isprime = False
            break
    return isprime
N = int(input())
if N % 2 != 0:
    exit(0)
for p in range(2,N):
    if isprime(p) == True:
        q = N - p
        if isprime(q) == True:
            print('{} = {} + {}'.format(N,p,q))
            break