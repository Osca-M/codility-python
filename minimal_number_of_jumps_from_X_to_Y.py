
def solution(X: int, Y: int, D: int) -> int:
    jumps = 0
    distance = Y-X
    while distance > 0:
        jumps += 1
        distance -= D
    return jumps
