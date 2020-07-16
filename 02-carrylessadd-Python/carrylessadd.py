# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.

import math


def fun_carrylessadd(x, y):
    res = 0
    multiplier = 1
    bit_sum = 0
    while (x or y):
        bit_sum = ((x % 10) + (y % 10))
        bit_sum = bit_sum % 10
        res = (bit_sum * multiplier) + res
        x = math.floor(x / 10)
        y = math.floor(y / 10)
        multiplier = multiplier * 10
    return res
