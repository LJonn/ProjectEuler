import math
maxNumber = 100000
amicableSum = 0


def sumOfDivisors(number):
    sum = 0
    for i in range(1, number):
        if (number % i == 0):
            sum += i
    return sum


for number in range(2, maxNumber):
    sum = sumOfDivisors(number)
    if (sumOfDivisors(sum) == number and number != sum):
        amicableSum += number
print(amicableSum)
