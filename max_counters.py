def solution(N: int, A: list) -> list:
    M = len(A)
    cs = [0] * N
    mr = mc = 0

    for ind in range(M):
        if A[ind] == N + 1:
            mr = max(mr, mc)
        else:
            if cs[A[ind] - 1] < mr:
                cs[A[ind] - 1] = mr

            cs[A[ind] - 1] += 1
            mc = max(mc, cs[A[ind] - 1])

    for ind in range(N):
        cs[ind] = max(mr, cs[ind])

    return cs
