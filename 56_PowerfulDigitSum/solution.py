def sum_digits(num):
    num_sum = 0
    while num > 0:
        digit = num % 10
        num_sum += digit
        num = num//10
    return num_sum


a_max = 100
b_max = 100
num_sums = set()

for a in range(a_max):
    for b in range(b_max):
        num_sums.add(sum_digits(a**b))

print(max(num_sums))
