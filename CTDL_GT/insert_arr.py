import math

n = int(input())
a = [i for i in range(1,n+1)]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


out = [i for i in a if is_prime(i)] 