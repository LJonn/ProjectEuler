import math
import matplotlib.pyplot as plt
import numpy as np

p_max = 1000
data = {}


def perimeter(a, b):
    return a+b+math.sqrt(a*a+b*b)


for a in range(1, p_max+1):
    b = 1
    p = perimeter(a, b)
    while (p <= p_max):
        p = perimeter(a, b)
        if (p % 1 == 0):
            if p in data:
                data[p]["count"] += 1
                data[p]["triangle"].append([a, b, math.sqrt(a*a+b*b)])
            else:
                data[p] = {"count": 1, "triangle": [a, b, math.sqrt(a*a+b*b)]}
        b += 1

max_p_key = max(data, key=lambda k: data[k]["count"])

print(max_p_key, data[max_p_key])

perimeters = np.array(list(data.keys()))
counts = np.array([data[p]["count"] for p in perimeters])

fig = plt.figure(figsize=(16, 6))
plt.bar(x=perimeters, height=counts, width=1)
plt.xlabel("Perimeter")
plt.ylabel("Number of Solutions")
plt.title("Number of Solutions for each Perimeter")
plt.savefig("histogram.png")
