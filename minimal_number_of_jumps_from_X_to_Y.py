import math


def solution(X: int, Y: int, D: int) -> int:
    distance = Y-X
    while distance > 0:
        multiples = (distance / D)
        if multiples > math.floor(multiples):
            return math.floor(multiples) + 1
        else:
            return math.floor(multiples)
    return 0
