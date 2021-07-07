# find the largest diff in the array, where the smaller number comes before the larger number
# [7, 8, 4, 9, 9, 15, 3, 1, 10]; // 11
def solution(a: list) -> int:
    n = len(a)
    result = a[1] - a[0]

    for i in range(0, n):
        for j in range(i + 1, n):
            if a[j] - a[i] > result:
                result = a[j] - a[i]
    return result
