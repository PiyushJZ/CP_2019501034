# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L
# contains any duplicate values (that is,
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
    # Your code goes here
    nums = {}
    for row in L:
        for num in row:
            if num in nums:
                return True
            nums[num] = 1
    return False


print(hasduplicates(
    [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 11]]))
