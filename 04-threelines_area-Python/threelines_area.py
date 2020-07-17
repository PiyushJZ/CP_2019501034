# Write the function fun_threelines_area(d1, d2, d3)
# that takes length of 3 sides
# find the area of a triangle(return an int) given its side lengths.

import math


def fun_threelines_area(a, b, c):
    hyp = a * a
    base = (c / 2) * (c / 2)
    height = math.sqrt(hyp - base)

    return = 0.5 * c * height
