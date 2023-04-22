import math

n = 35
def prime_factors(n):
    a = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            a.append(i)
            n /= i
    return a
    
print(prime_factors(n))

pfactor = sum(prime_factors(n))
print(pfactor)

def prime(pfactor):
    a = []
    for i in range(2, int(math.sqrt(pfactor)) + 1):
        while pfactor % i == 0:
            a.append(i)
            pfactor /= i
    return a

print(sum(prime(pfactor)))