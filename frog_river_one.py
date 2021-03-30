def solution(A: list, X: int) -> int:
    lc, ss = [False] * X, 0
    for k, v in enumerate(A):
        if v > X:
            continue
        if not lc[v - 1]:
            lc[v - 1] = True
            ss += 1
            if ss == X:
                return k
    return -1
