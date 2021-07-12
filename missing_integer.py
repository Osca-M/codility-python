# write your code in Python 3.6
# Find the smallest positive integer that does not occur in a given sequence.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Given A = [1, 3, 6, 4, 1, 2], the function should return 5

def solution(A: list) -> int:
    ln = len(A)
    if 1 not in A:
        return 1

    if len(A) == 1:
        return 2 if A[0] == 1 else 1
    total = ln * (ln + 1) / 2
    if total - sum(set(A)) == 0:
        return max(A) + 1
    for x in range(1, len(A)):
        if x not in A:
            return x
