import math


def combination(n: int, r: int) -> int:
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))


count = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if (combination(n, r) > 10**6):
            count += 1
print(count)
