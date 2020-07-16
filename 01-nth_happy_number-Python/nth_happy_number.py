# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


def fun_nth_happy_number(n):
    c = 0
    latest = 0
    num = 1
    while c != n:
        sum = 0
        num1 = num
        while sum != 1 and sum != 4:
            sum = 0
            while num1 != 0:
                rem = num1 % 10
                sum += (rem * rem)
                num1 //= 10
            num1 = sum

        if sum == 1:
            c += 1
            latest = num

        num = num + 1
    return latest
