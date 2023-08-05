import math


def isPrime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num+1))+1):
        if num % i == 0:
            return False
    return True


def generateNextPrime(num: int) -> int:
    while (True):
        num += 1
        if isPrime(num):
            return num


def conjectureHolds(oddCompositeNum: int, primes: list[int]) -> bool:
    while oddCompositeNum >= max(primes):
        primes.append(generateNextPrime(max(primes)))
    for prime in primes:
        i = 1
        while (prime+2*i*i < oddCompositeNum):
            i += 1
        if (prime+2*i*i == oddCompositeNum):
            return True
    return False


def isOddComposite(num: int) -> bool:
    if num % 2 == 0 or isPrime(num):
        return False
    return True


checkedPrimes = [2, 3, 5, 7]

oddNum = 33
while (True):
    oddNum += 2
    if (isOddComposite(oddNum) and not conjectureHolds(oddNum, checkedPrimes)):
        print(oddNum)
        break
