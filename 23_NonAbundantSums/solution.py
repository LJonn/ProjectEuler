def isAbundant(number):
    isAbundant = False
    divisorsSum = 0
    for j in range(1, number):
        if (number % j == 0):
            divisorsSum += j
    if (divisorsSum > i):
        isAbundant = True
    return isAbundant


upper = 28123
abundantSums = set()
abundantList = []
for i in range(1, upper):
    if (isAbundant(i)):
        abundantList.append(i)

for i in range(len(abundantList)):
    for j in range(i, len(abundantList)):
        abundantSums.add(abundantList[i]+abundantList[j])

sum = 0
for i in range(1, upper):
    if (i not in abundantSums):
        sum += i
print(sum)
