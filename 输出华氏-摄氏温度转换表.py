lower , upper = input().split()
lower , upper = eval(lower) , eval(upper)
if lower > upper:
    print("Invalid.")
else:
    print("fahr celsius")
    i = lower
    while i <= upper:
        print("{:d}{:>6.1f}".format(i,5*(i-32)/9))
        i += 2
