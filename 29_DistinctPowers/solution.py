size = 100
answerSet = set()
for i in range(2, size+1):
    for j in range(2, size+1):
        answerSet.add(i**j)

print(len(answerSet))
