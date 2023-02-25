import math

nm1 = 1
nm2 = 1
n = nm1+nm2
i = 3
while (len(str(n)) < 1000):
    i += 1
    nm2 = nm1
    nm1 = n
    n = nm1+nm2
print(i)

print(math.ceil((999+math.log10(5)/2)/math.log10((1+math.sqrt(5))/2)))
