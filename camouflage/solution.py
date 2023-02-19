with open("pair.txt") as file:
    pairFile = file.read()
    pair = pairFile.split()
    a = int(pair[0])
    b = int(pair[1])


def firstLast(number):
    sizeOfNumber = len(str(number))
    firstDigit = number//(10 ** (sizeOfNumber-1))
    lastDigit = number % 10
    return [firstDigit, lastDigit]


[a1, an] = firstLast(a)
while (a1 != an):
    a += 1
    [a1, an] = firstLast(a)

[b1, bn] = firstLast(b)
while (b1 != bn):
    b -= 1
    [b1, bn] = firstLast(b)


def countOfCorrect(number):
    count = 0
    length = len(str(number))
    lastDigit = number % 10
    for place in range(1, length+1):
        if (place != length):
            if (place < 3):
                count += 9
            else:
                count += 9*10**(place-2)
        else:
            if (place < 3):
                count += lastDigit
            else:
                insideNumber = (number % (10**(place-1)))//10
                count += (lastDigit-1)*10**(place-2)+insideNumber+1
    return count


print(a)
print(b)
bx = countOfCorrect(b)
ax = countOfCorrect(a)
print(bx-ax+1)
