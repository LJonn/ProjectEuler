length_limit = 10**6+2
number = "0."
i = 1
while (len(number) < length_limit):
    number += str(i)
    i += 1

answer = 1
for i in range(7):  # 7 things to multiply
    answer *= int(number[10**i+1])
    # i=0 | index=2
    # i=1 | index=11

print(answer)
