error = float(input())
e2 = 2
e1 = 1
x = 1
sum = 2
i = 2
j = 2
y = 1/j
while e2 - e1 >= error:
    e1 = e2
    x = y
    sum = sum + x
    e2 = sum
    i += 1
    j = j*i
    y = 1/j
print('%.6f' % e2)
    
    