import time
import itertools

start = time.time()


def listToInt(arr):
    number = 0
    for digit in arr:
        number = number*10+digit
    return number


def productAndFilter(unusedNumbers, numList, divisor):
    filteredNums = filter(lambda t: listToInt(
        (t[0], *t[1])[:3]) % divisor == 0, itertools.product(unusedNumbers, [numList]))
    filteredNums = [(i[0], *i[1]) for i in filteredNums]
    return filteredNums


def extendNumbersByOneDigit(nums, divisor):
    result = []
    for num in nums:
        unusedNumbers = filter(lambda x: x not in num, range(10))
        newNums = productAndFilter(unusedNumbers, num, divisor)
        result.extend(newNums)
    return result


divisors = [2, 3, 5, 7, 11, 13]

generatedNumbers = filter(lambda elements: listToInt(elements) %
                          17 == 0, itertools.permutations(range(10), 3))

for div in reversed(divisors):
    generatedNumbers = extendNumbersByOneDigit(generatedNumbers, div)

print(sum(listToInt(i) for i in generatedNumbers))
for num in generatedNumbers:
    print(num)

end = time.time()
print("{:.2f}".format((end-start)*1000), 'ms')
