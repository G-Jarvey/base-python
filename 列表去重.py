s = eval(input())
t = list(set(s))
t.sort(key = s.index)
for i in range(len(t)):
    if i != len(t)-1:
        print(t[i],end=' ')
    else:
        print(t[i])