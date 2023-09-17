import math
import itertools


def isPrime(number: int):
    if number == 2:
        return True
    if number < 2:
        return False
    for i in range(2, math.floor(math.sqrt(number))+2):
        if ((number/i).is_integer()):
            return False
    return True


def nextPrime(num: int):
    while (not isPrime(num+1)):
        num += 1
    return num+1


def numberOfPrimes(digits):
    change_indexes = []
    i_min = 0
    result = 0
    for index, digit in enumerate(digits):
        if type(digit) == str:
            change_indexes.append(index)

    if (change_indexes[0] == 0):
        i_min = 1

    for i in range(i_min, 10):
        for index in change_indexes:
            digits[index] = i

        number = 0
        for index, digit in enumerate(reversed(digits)):
            number = number+digit*10**index

        if (isPrime(number)):
            result += 1
    return result


def numToList(num):
    result = []
    result.append(num % 10)
    num = num//10
    while (num > 0):
        result.append(num % 10)
        num = num//10
    return list(reversed(result))


def applyTemplate(nums, template):
    result = []
    for i, n in enumerate(nums):
        if (template[i] == "*"):
            result.append("*")
        else:
            result.append(nums[i])
    return result


def isLowestTemplate(digits, template):
    minNum = 0
    if type(template[0]) == str:
        minNum = 1
    for i, digit in enumerate(digits):
        if template[i] == "*":
            if (digit != minNum):
                return False
    return True


primeNumber = 7
finished = False
while (not finished):
    primeNumber = nextPrime(primeNumber)
    length = len(numToList(primeNumber))
    templates = list(itertools.product('*C', repeat=length))
    templates = templates[:-1]
    for template in templates:
        numDigits = numToList(primeNumber)
        if (isLowestTemplate(numDigits, template)):
            templated = applyTemplate(numDigits, template)
            if (numberOfPrimes(templated)) == 8:
                print(primeNumber, template)
                finished = True
                break
