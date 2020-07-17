# Write the function alternatingSum(a) that takes a list of numbers and returns the
# alternating sum (where the sign alternates from positive to negative or vice versa).
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.


def fun_alternatingsum(a):
    if len(a) == 0:
        return 0
    sum = 0
    sign = False
    for i in a:
        if sign:
            sum -= i
            sign = False
        else:
            sum += i
            sign = True
    return sum
