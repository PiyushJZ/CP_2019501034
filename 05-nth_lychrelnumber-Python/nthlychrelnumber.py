# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
    # your code goes here
    count = 0
    num = 0
    while count != n:
        num += 1
        if isLychrel(num):
            count += 1
    return num


def isLychrel(n):
    for i in range(MAX_ITERATIONS):
        n = n + reverse(n)
        if (isPalindrome(n)):
            return "false"
    return "true"


def isPalindrome(n):
    return n == reverse(n)


def reverse(n):
    reverse = 0
    while (n > 0):
        remainder = n % 10
        reverse = (reverse * 10) + remainder
        n = int(n / 10)
    return reverse
