import math
from array import array


def isLeapYear(year):
    isLeapYear = False
    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        isLeapYear = True
    return isLeapYear


monthlyDays = array("i", [31, 29 if isLeapYear(
    1900) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
weekDay = 1
for daysInMonth in monthlyDays:
    weekDay = (weekDay+daysInMonth) % 7
# print(weekDay)

counter = 0
for i in range(1901, 2001):
    monthlyDays = array("i", [31, 29 if isLeapYear(
        1900) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    for daysInMonth in monthlyDays:
        weekDay = (weekDay+daysInMonth) % 7
        if (weekDay == 0):
            counter += 1

print(counter)
