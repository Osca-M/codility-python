from collections import deque


def solution(A: list, K: int) -> list:
    queue = deque(A)
    while A:
        for i in range(K):
            queue.appendleft(queue[-1])
            queue.pop()
        return list(queue)
    return []
