import time

start_time = time.time()
length_limit = 10**6
digits = []
i = 1
while (len(digits) < length_limit):
    # digits += str(i) # bad code, concatenating slow
    digits.extend(str(i))
    i += 1

answer = 1
for i in range(7):  # 7 things to multiply
    index = 10**i-1
    # i=0 | index=0
    # i=1 | index=9
    # i=2 | index=99
    answer *= int(digits[index])


end_time = time.time()

print(end_time-start_time)
# old time 4.1 s
# new time 0.1 s
print(answer)
