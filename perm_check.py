# Check whether array A is a permutation. A permutation is a sequence containing each element from 1 to N once,
# and only once.
# Given [4, 1, 3, 2] = 1
# Given [4, 1, 3] = 0


def solution(A: list) -> int:
    if len(set(A)) == len(A):
        if list(set(A))[-1] == len(set(A)):
            return 1
    return 0
