a = float(input())
if 0<=a<=50:
    print("cost = {:.2f}".format(a*0.53))
elif a>50:
    print("cost = {:.2f}".format(50*0.53+(a-50)*0.58))
else:
    print("Invalid Value!")
