lst = eval(input())
def f(lst,level):
    sum = 0
    for i in lst:
        if type(i) == int:
            sum = sum + i*level #最底层为int，加权和
        else:
            sum = sum + f(i,level+1)#未到最底层则继续向下
    return sum
sum = f(lst,1)
print(sum)