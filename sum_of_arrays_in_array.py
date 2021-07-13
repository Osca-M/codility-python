# Write a function that takes as input an array and outputs the sum of all of its subarrays.
# For example, given [1, 3, 7] = 36

def solution(a: list) -> int:
    """
        from itertools import combinations
        y = [a[s:e] for s, e in combinations(range(len(a) + 1), 2)]
        another generator solution
    """
    n = len(a)
    temp, result = 0, 0

    # Pick starting point
    for i in range(0, n):
        # Pick ending point
        temp = 0
        for j in range(i, n):
            # sum subarray between current starting and ending points
            temp += a[j]
            result += temp
    return result
