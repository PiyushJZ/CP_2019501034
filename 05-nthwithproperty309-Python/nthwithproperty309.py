# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.

def nthwithproperty309(n):
    # Your code goes here
    count = 0
    num = 308
    while count != n:
        num += 1
        if isWithProperty309(num):
            count += 1
    return num


def isWithProperty309(n):
    num = n ** 5
    num = str(num)
    for i in range(10):
        if i not in num:
            return False
    return True
