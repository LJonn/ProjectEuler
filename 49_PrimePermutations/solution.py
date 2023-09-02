def is_prime(num):
    if (num < 2):
        return False
    for i in range(2, int(num**(1/2))+1):
        if (num % i == 0):
            return False
    return True


def arePermutations(numbers):
    sorted_numbers = [''.join(sorted(str(num))) for num in numbers]
    return all(sorted_numbers[0] == num for num in sorted_numbers)


primeList = list()
for i in range(1000, 10000):
    if is_prime(i):
        primeList.append(i)

maxPrime = primeList[-1]
for i, prime in enumerate(primeList):
    for j in range(i+1, len(primeList)):
        delta = primeList[j]-prime
        if ((primeList[j]+delta) in primeList and arePermutations([prime, primeList[j], primeList[j]+delta])):
            print(prime, " ", primeList[j], " ", (primeList[j]+delta))
