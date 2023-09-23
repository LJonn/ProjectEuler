def numToArray(num: int) -> list[int]:
    result = []
    while (num//10 != 0):
        result.append(num % 10)
        num = num//10
    result.append(num % 10)
    return list(reversed(result))


def containsSame(num1: int, num2: int) -> bool:
    num1_array = numToArray(num1)
    num2_array = numToArray(num2)
    if (set(num1_array) == set(num2_array) and len(num1_array) == len(num2_array)):
        return True
    return False


num = 0
containsAll = False

while not containsAll:
    num += 1
    if numToArray(num)[0] != 1:
        continue
    for i in range(1, 6):
        containsAll = all(containsSame(num*i, num*(i+1)) for i in range(1, 6))

print(num)
