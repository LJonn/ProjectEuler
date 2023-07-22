import math
def calculate_pentagonal(n: int) -> int:
    return (n*(3*n-1)//2)

def is_pentagonal(num: int) -> bool:
    return (((1+math.sqrt(1+24*num))/6)%1==0)

checked_pentagonals=[1]
i_next_pentagonal=1
answered=False
while not answered:
    next_pendagonal=calculate_pentagonal(i_next_pentagonal)
    for i_checked, checked in enumerate(checked_pentagonals):
        if(is_pentagonal(next_pendagonal-checked) and is_pentagonal(next_pendagonal+checked)):
            print("P1: (i, value)", i_checked, checked)
            print("P2: (i, value): ", i_next_pentagonal, next_pendagonal)
            print("P2-P1: ", next_pendagonal-checked)
            answered=True
            break
    checked_pentagonals.append(next_pendagonal)
    i_next_pentagonal+=1