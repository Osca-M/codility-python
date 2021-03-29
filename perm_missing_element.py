def solution(A: list) -> int:
    if not all(isinstance(x, int) for x in A):
        raise ValueError("List does not contain integers only")
    ln = len(A) + 1
    possible_sum = ln * (ln + 1) / 2
    total = sum(A)
    return int(possible_sum - total)
