# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    count = {}
    for alpha in s:
        if alpha not in count:
            count[alpha] = s.count(alpha)
            # print(s.count(alpha))
    for i in count:
        # print(i, count[i])
        if count[i] == n:
            return i
    return None
