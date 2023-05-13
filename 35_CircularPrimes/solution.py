limit = 10**6
primeNumbersBelowLimit = 0
def isPrime(number):
    if (number <= 1):
        return False
    for x in range(2, int(number**(1/2)) + 1):
        if (number % x == 0):
            return False
    return True

def rotate(number):
        numStr=str(number)
        newNum = ""
        for i in range(len(numStr)):
                newNum+=numStr[i-1]
        return int(newNum)
  

for i in range(limit):
        if isPrime(i):
                checkedNumberIsPrime = True
                checkedNumber = i
                for j in range(len(str(i))-1):
                        checkedNumber = rotate(checkedNumber)
                        checkedNumberIsPrime = isPrime(checkedNumber)
                        if (not checkedNumberIsPrime):
                                break
                if (checkedNumberIsPrime):
                        print(i)
                        primeNumbersBelowLimit+=1

print(primeNumbersBelowLimit)