import math


def isPrime(num: int):
    if num == 2:
        return True
    if num < 2:
        return False
    for i in range(2, math.floor(math.sqrt(num))+2):
        if ((num/i).is_integer()):
            return False
    return True


def nextPrime(num: int):
    while (not isPrime(num+1)):
        num += 1
    return num+1


prime_list = []
prime = 2
while sum(prime_list)+prime < 10**6:
    prime_list.append(prime)
    prime = nextPrime(prime)

found = False
for i in range(len(prime_list)//2):
    for j in range(i+1):
        if isPrime(sum(prime_list[j: len(prime_list)-i+j])):
            print(sum(prime_list[j: len(prime_list)-i+j]))
            found = True
        if found:
            break
    if found:
        break
