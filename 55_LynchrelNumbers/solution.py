def isPalindrome(num):
    if num == 0:
        raise ValueError("Can't be zero")
    digits = []
    while num != 0:
        digits.append(num % 10)
        num = num//10
    for i, digit in enumerate(digits):
        if digit != digits[-i-1]:
            return False
    return True


def numLenght(num):
    length = 0
    if num == 0:
        return 1
    while num != 0:
        num = num//10
        length += 1
    return length


def reverse(num):
    revNum = 0
    length = numLenght(num)
    while num != 0:
        length -= 1
        revNum += num % 10*10**length
        num = num//10
    return revNum


def isLynchrel(num, max_depth):
    nextNum = num+reverse(num)
    for i in range(max_depth):
        if isPalindrome(nextNum):
            return False
        nextNum = nextNum+reverse(nextNum)
    return True


max_num = 10000
max_depth = 50

count = 0
for num in range(1, max_num):
    if isLynchrel(num, max_depth):
        count += 1

print(count)
