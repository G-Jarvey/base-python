str1 = input()
s = input()
str2 = list(s)
t = 0
for i in range(len(s)-1,-1,-1):
    if str2[i] == str1:
        print("index =",i)
        break
    if i == 0:
        print('Not Found')
