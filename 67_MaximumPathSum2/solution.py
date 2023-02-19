import math
from array import array
import numpy as np
with open("p067_triangle.txt") as file:
    pyramid_string = file.read()
    pyramid_list = pyramid_string.split("\n")
    pyramid = [int(x) for line in pyramid_list for x in line.split()]


def pyramidElement(pyramid, row, column):
    index = int(row*(1+row)/2) + column
    return pyramid[index]


def getNumberOfLevels(pyarmid):
    return int((math.sqrt(1+8*len(pyarmid))-1)/2)


pyramidLevels = getNumberOfLevels(pyramid)
sumArray = array("i", [0]*pyramidLevels)
for level in range(pyramidLevels):
    for column in range(level, -1, -1):
        if (column != 0 and sumArray[column-1] > sumArray[column]):
            sumArray[column] = sumArray[column-1] + \
                pyramidElement(pyramid, level, column)
        else:
            sumArray[column] += pyramidElement(pyramid, level, column)

print(max(sumArray))
