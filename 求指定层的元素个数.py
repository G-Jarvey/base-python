lst = eval(input())
n = int(input())
def f(lst,level):
    sum = 0
    for i in lst:
        if type(i) == int:
            if level == n:
                sum = sum + 1
        else:
            sum = sum + f(i,level+1)
    return sum
sum = f(lst,1)
print(sum)