# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
    for sub_arr in l:
        for num in sub_arr:
            if isPrime(num):
                return False
    return True


def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, n):
        if (n % i == 0):
            return False
    return True


print(fun_hasnoprimes([[9, 12], [8], [16, 8, 19]]))
