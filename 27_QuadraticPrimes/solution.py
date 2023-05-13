limit = 1000


# function is number prime
def isPrime(number):
    if (number < 0):
        return False
    for x in range(2, int(number**(1/2)) + 1):
        if (number % x == 0):
            return False
    return True


# fn number of primes for coef (a,b)
def generatorQuality(a, b):
    n = 0
    while (isPrime(n**2+a*n+b)):
        n = n+1
    return n


# find longest prime generator coefficients
amax = 0
bmax = 0
bigQ = 0
for a in range(-limit+1, limit):
    for b in range(-limit, limit+1):
        newQ = generatorQuality(a, b)
        if (newQ > bigQ):
            bigQ = newQ
            amax = a
            bmax = b

# Multiply a*b
print(amax, bmax, amax*bmax, bigQ)
