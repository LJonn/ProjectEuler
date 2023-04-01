sumsum = 0
# 6 * 9**5 == 354294, so, max 6 digits
for number in range(2, 354294):
    numberAsString = str(number)
    sum = 0
    for numberChar in numberAsString:
        sum += int(numberChar)**5
    if (sum == number):
        print(number)
        sumsum += sum
print("Sum of all numbers where their digits to the power of 5 sum is the number itself:", sumsum)
