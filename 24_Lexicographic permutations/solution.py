import math


def permutation(n, permutationNr):
    permutation = []
    unusedNumbers = [i for i in range(n)]
    nFac = math.factorial(n)
    for i in range(n):
        index = (permutationNr-1) % nFac
        nFac = nFac//(n-i)
        index = index//nFac
        number = unusedNumbers[index]
        permutation.append(number)
        unusedNumbers.remove(number)
    return "".join(str(num) for num in permutation)


print(permutation(10, 1000000))
