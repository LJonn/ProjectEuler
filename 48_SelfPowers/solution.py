answ = 0

for i in range(1, 1001):
    answ += pow(i, i, 10**10)
    answ = answ % 10**10

print(answ)
