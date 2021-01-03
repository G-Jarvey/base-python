def prime(p):
    for i in range(2,p):
        if p%i == 0:
            return False
    if p!=1:
        return True
def PrimeSum(m,n):
    sum = 0
    for i in range(m,n+1):
        if prime(i):
            sum = sum + i
    return sum
