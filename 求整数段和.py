A,B = input().split()
A = int(A)
B = int(B)
x = 0
for i in range(A,B+1):
    x += i
    print("{:5d}".format(i),end='')
    if (i-A)%5==4:
        print()
if (B-A+1)%5!=0:
        print()
print('Sum =',x)
