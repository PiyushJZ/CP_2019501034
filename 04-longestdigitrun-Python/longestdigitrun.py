# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
def longestdigitrun(n):
    # Your code goes here
    num = str(abs(n))
    count = 0
    max_count = 1
    nums = []
    for i in range(1, len(num)):
        if num[i] == num[i - 1]:
            count += 1
        else:
            if count > max_count:
                print(count, max_count)
                max_count = count
                nums = []
                nums.append(num[i - 1])
            elif count == max_count:
                nums.append(num[i - 1])
            count = 0
    nums.sort()
    return nums[0]
