string = input()
str1 = input()
dic = {}
for i in string:
    dic[i] = dic.get(i,0)+1
print(dic.get(str1,0))