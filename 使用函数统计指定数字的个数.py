def CountDigit(number,digit):
    num = str(number)
    dig = str(digit)
    lis = list(num)
    count = 0
    for i in lis:
        if dig == i:
            count += 1
    return count
