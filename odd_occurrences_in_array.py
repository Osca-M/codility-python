from collections import Counter


def solution(A: list) -> int:
    if not all(isinstance(x, int) for x in A):
        raise ValueError("List does not contain integers only")
    while A:
        items_count = dict(Counter(A))
        for k, v in items_count.items():
            if v % 2 != 0:
                return int(k)
    return None
