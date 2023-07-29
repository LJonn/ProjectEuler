import math


def calculate_hexagonal(n: int) -> int:
    return n*(2*n-1)


def hexagonalIsPentagonal(h: int):
    p = (1+math.sqrt(1+24*(2*h**2-h)))/6
    return p.is_integer()


numberOfResults = 1
start_n = 144
while (numberOfResults != 0):
    if (hexagonalIsPentagonal(start_n)):
        print(calculate_hexagonal(start_n))
        numberOfResults -= 1
    start_n += 1
