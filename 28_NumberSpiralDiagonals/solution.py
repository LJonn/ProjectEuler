num = 1
sum = 1
squareDimensions = 1001

for i in range(1, int((squareDimensions-1)/2)+1):
    for j in range(1, 5):
        num = num+2*i
        sum = sum+num

print(sum)
