def getSum(n):
    sum = 0
    for digit in str(n):
        sum+= int(digit)
    return sum
n = 123
print(getSum(n))