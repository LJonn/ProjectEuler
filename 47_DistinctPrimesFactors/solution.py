import math


def primeFactors(num):
    factors = set()
    for i in range(2, int(math.sqrt(num)+3)):
        while (num % i == 0 and num != 0):
            factors.add(i)
            num = int(num/i)
    if (num > 1):
        factors.add(num)
    return factors


i = 6
consecutive = 0
answer = list()
while (True):
    i += 1
    factors = primeFactors(i)
    if (len(factors) == 4):
        answer.append(i)
        consecutive += 1
    else:
        answer.clear()
        consecutive = 0
    if (consecutive == 4):
        break
print(answer)
