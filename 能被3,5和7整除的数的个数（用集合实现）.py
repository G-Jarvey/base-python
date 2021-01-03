a,b = input().split()
a = int(a)
b = int(b)
s1 = set()
s2 = set()
s3 = set()
for i in range(a,b+1):
    if i%3 == 0:
        s1.add(i)
    if i%5 == 0:
        s2.add(i)
    if i%7 == 0:
        s3.add(i)
s = set(s1 & s2 & s3)
print(len(s))