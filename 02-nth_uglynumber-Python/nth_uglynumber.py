# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    if not n:
        return 1
    i = 1
    count = 1
    while n > count:
        if isUgly(i):
            count += 1
        i += 1
    return i


def isUgly(n):
    if (n == 1):
        return 1
    if (n <= 0):
        return 0

    if (n % 2 == 0):
        return (isUgly(n // 2))

    if (n % 3 == 0):
        return (isUgly(n // 3))

    if (n % 5 == 0):
        return (isUgly(n // 5))

    return 0
