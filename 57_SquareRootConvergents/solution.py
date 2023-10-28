import sys
from fractions import Fraction as Fr
sys.setrecursionlimit(1010)


def calc_root2(iterations):
    return 1+calc_root_recusrive(1, iterations)


def calc_root_recusrive(current_i, iterations):
    if current_i >= iterations:
        return Fr(1, 2)
    return Fr(1, 2+calc_root_recusrive(current_i+1, iterations))


def countDigits(num):
    count = 0
    if num == 0:
        return 1
    while num > 0:
        num = num//10
        count += 1
    return count


iterations = 1000
answer = 0
for i in range(1, iterations+1):
    fraction = calc_root2(i)
    if countDigits(fraction.numerator) > countDigits(fraction.denominator):
        answer += 1
print(answer)
