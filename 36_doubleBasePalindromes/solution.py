limit = 10**6
counter=0
sum=0

def isPolindrome(inputString):
    halfSize=len(inputString)//2
    for index in range (0, halfSize):
        if (inputString[index]!=inputString[-index-1]):
            return False
    return True

for number in range(1,limit):
    decimalNumberString = str(number)
    if (isPolindrome(decimalNumberString)):
        binaryNumberString = str(bin(number)).removeprefix("0b")
        if (isPolindrome(binaryNumberString)):
            counter+=1
            sum+=number
            
print(counter, sum)