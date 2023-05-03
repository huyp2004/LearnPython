def check_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


my_list = [1, 7, 5, 3, 8, 90, 6, 4, 6, 1]

prime = [i for i in my_list if check_prime(i)]

prime.sort()

print(prime)
