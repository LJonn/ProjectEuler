def isPrime(number):
    if (number <= 1):
        return False
    for x in range(2, int(number**(1/2)) + 1):
        if (number % x == 0):
            return False
    return True

count = 0
number = 10
truncPrimeSum = 0
while (count < 11):
    number += 1
    if (isPrime(number)):
        numStr = str(number)
        length = len(numStr)
        theChosenOne = True
        for i in range(1,length):
            if (not isPrime(int(numStr[i:length])) or
                not isPrime(int(numStr[0:length-i]))):
                    theChosenOne = False
                    break
        if (theChosenOne):
            print(number)
            truncPrimeSum+=number
            count+=1
print(truncPrimeSum)