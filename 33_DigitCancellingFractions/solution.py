def simplify(x, y):
    for i in range(y, 1, -1):
        if (x % i == 0 and y % i == 0):
            return (True, int(x/i), int(y/i))
    return (False, x, y)


def findCommon(x, y):
    for i in str(x):
        if i in str(y):
            return int(i)
    return -1


answerFractions = set()

for x in range(10, 100):
    for y in range(x+1, 100):
        numbers = set()
        for i in (str(x)+str(y)):
            numbers.add(i)
        if (len(numbers) == 3 and x % 10 != 0):
            commonNumber = findCommon(x, y)
            if (commonNumber >= 0):
                xReduced = int(str(x).replace(str(commonNumber), ""))
                yReduced = int(str(y).replace(str(commonNumber), ""))
                if (yReduced != 0 and x/y == xReduced/yReduced):
                    print(str(x)+"/"+str(y) + "=>" +
                          str(xReduced)+"/"+str(yReduced))
                    answerFractions.add(simplify(xReduced, yReduced))

productX = 1
productY = 1
for i in answerFractions:
    productX *= i[1]
    productY *= i[2]

print(simplify(productX, productY))
