def repeatingDecimal(denominator):
    numerator=1
    i=0
    count=0
    numerators=[]
    while (numerator%denominator != 0):
        if (numerator//denominator!=0):
            if(numerator in numerators):
                count=i-numerators.index(numerator)
                break
            numerators.append(numerator)
            numerator%=denominator
        else:
            numerator*=10
            if(len(numerators)!=0):
                i+=1
    return count

size=0
number=0 
for d in range(2,1000): 
    period=repeatingDecimal(d)
    if(period>size):
        size=period
        number=d

print(number, size)
