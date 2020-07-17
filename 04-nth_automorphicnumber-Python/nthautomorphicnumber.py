# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6,
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
    # Your code goes here
    count = 0
    num = 0
    while count != n:
        num += 1
        if isAutoMorphic(num):
            count += 1
    return n


def isAutoMorphic(n):
    sqr = n ** 2
    a = str(n)
    b = str(sqr)
    l1 = len(a)
    l2 = len(b)
    return l2 - b.find(a) == l1
