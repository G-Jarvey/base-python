lst = eval(input())
def f(lst,level):
    sum = 0
    for i in lst:
        if type(i) == int:
            sum = sum + level
        else:
            sum = sum + f(i,level+1)
    return sum
sum = f(lst,1)
print(sum)