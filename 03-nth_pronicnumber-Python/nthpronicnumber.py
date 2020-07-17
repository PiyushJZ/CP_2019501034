# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

import math


def nthpronicnumber(n):
    # Your code goes here
    count = 0
    i = 0
    while count != n:
        i += 1
        if checkPronic(i):
            count += 1
    return i


def checkPronic(x):
    i = 0
    while (i <= (int)(math.sqrt(x))):
        if (x == i * (i + 1)):
            return True
        i = i + 1

    return False
