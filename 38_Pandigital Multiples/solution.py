largestNumber = 0
aMax = 9876


def isPandigital(numberStr):
    if (len(numberStr) != 9):
        return False
    else:
        digits = set(numberStr)
        return len(digits) == 9 and '0' not in digits


for a in range(1, aMax):
    c = 1
    catNumber = str(a)
    while (len(catNumber) < 9):
        c += 1
        catNumber += str(c*a)
    if (isPandigital(catNumber) and int(catNumber) > largestNumber):
        largestNumber = int(catNumber)
        print(a, c)

print(largestNumber)
