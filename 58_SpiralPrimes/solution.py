import math


def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, math.floor(math.sqrt(num)+1)):
        if (num/i).is_integer():
            return False
    return True


def count_prime_spiral_corners(side_length):
    counter = 0
    for i in range(1, 4):
        if is_prime(side_length**2-i*(side_length-1)):
            counter += 1
    return counter


side_length = 3
count_diagonal = 5
count_prime_diagonal = 3
while count_prime_diagonal/count_diagonal > 0.1:
    side_length += 2
    count_diagonal += 4
    count_prime_diagonal += count_prime_spiral_corners(side_length)


print(side_length)
