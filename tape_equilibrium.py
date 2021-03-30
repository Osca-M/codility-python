from itertools import accumulate


def solution(A: list) -> int:
    if not all(isinstance(x, int) for x in A):
        raise ValueError("List does not contain integers only")
    s = sum(A)
    li = accumulate(A[:-1])
    return min([abs(2 * x - s) for x in li])
