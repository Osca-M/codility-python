# A function that, given three integers A, B and K, returns the number of integers within the range [A..B]
# that are divisible by K


def solution(A: int, B: int, K: int) -> int:
    L = [i for i in range(A, B + 1, K) if i != 0]
    return len(L)
