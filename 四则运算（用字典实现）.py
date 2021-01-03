n = int(input())
p = input()
m = int(input())
if m != 0:
    t = {'+': n+m, '-': n-m, '*': n*m, '/': n/m}
    result = t.get(p)
    print('%.2f'% result)
else:
    print('divided by zero')