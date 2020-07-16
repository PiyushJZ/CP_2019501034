# Write the function matrixMultiply(m1, m2) that takes two 2d lists
# (that we will consider to be matrices) and returns a new 2d list that
# is the result of multiplying the two matrices. Return None if the
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    row_1 = len(m1)
    col_1 = len(m1[0])
    row_2 = len(m2)
    col_2 = len(m2[0])
    if col_1 != row_2:
        return None
    result = [[0 for x in range(col_2)] for y in range(row_1)]
    for obj_x in range(row_1):
        for obj_y in range(col_2):
            for obj_z in range(row_2):
                result[obj_x][obj_y] += m1[obj_x][obj_z] * m2[obj_z][obj_y]
    return result
