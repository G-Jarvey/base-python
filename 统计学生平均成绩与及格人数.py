m = int(input())
if m != 0:
    n = map(int,input().split())
    n = list(n)
    sum = 0
    average = 0
    count = 0
    if m == 0:
        average = 0
        count = 0
    else:
        for i in n:
            if i >= 60:
                count += 1
            sum = sum + i
        average = sum/m
    print('average = %.1f' % average)
    print('count = %d' % count)
else:
    print('average = 0.0')
    print('count = 0')