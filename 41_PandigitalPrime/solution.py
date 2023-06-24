import math

def is_prime(num):
    if (num<2):
        return False
    for i in range(2, int(num**(1/2))+1):
        if (num%i == 0):
            return False
    return True

def permutate(num):
    numList = []
    digits = [int(digit) for digit in str(num)]
    length=len(digits)
    for i in range(math.factorial(length)):
        digits_copy=digits.copy()
        length_copy=length
        number=0
        while (length_copy>0):
            index=i//math.factorial(length_copy-1)%length_copy
            number += digits_copy[index]*(10**(length_copy-1))
            del digits_copy[index]
            length_copy-=1
        numList.append(number)
    return numList

#all pandigital numbers from 8 and 9 digits are divisable by 3 because their sum is divisable by 3.
for pandigital in permutate(7654321):
    if(is_prime(pandigital)):
        print(pandigital)
        break