# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


import math


def fun_nth_lefttruncatableprime(n):
    count = 0
    num = 0
    while count != n:
        if is_left(num):
            count += 1
        num += 1
    return num


def is_left(n):
    temp = n
    cnt = 0

    while (temp != 0):
        cnt = cnt + 1
        temp1 = temp % 10
        if (temp1 == 0):
            return False

        temp = temp // 10
    isPrime = [None] * (n + 1)
    check_left(n, isPrime)

    for i in range(cnt, 0, -1):
        mod = power(10, i)

        if (isPrime[n % mod] != True):
            return False
    return True


def check_left(n, isPrime):
    isPrime[0] = isPrime[1] = False
    for i in range(2, n+1):
        isPrime[i] = True
    p = 2
    while(p * p <= n):
        if (isPrime[p] == True):
            i = p*2
            while(i <= n):
                isPrime[i] = False
                i = i + p

        p = p + 1


def power(x, y):

    if (y == 0):
        return 1
    elif (y % 2 == 0):
        return(power(x, y // 2) * power(x, y // 2))
    else:
        return(x * power(x, y // 2) * power(x, y // 2))
