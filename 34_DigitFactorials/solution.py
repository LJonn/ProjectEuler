import math
answer = 0
for i in range(10, 9000000):
    sum = 0
    for j in str(i):
        sum += math.factorial(int(j))
    if (sum == i):
        print(i)
        answer += i
print(answer)
