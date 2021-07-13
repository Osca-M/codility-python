# Find the minimal average of any slice containing at least two elements.
import array
from itertools import combinations
import random
import string

def solution(A: array) -> int:
    print(len(A), "A")
    myD = {s: sum(A[s:e + 1]) / len(A[s:e + 1]) for s, e in combinations(range(len(A) + 1), 2)}
    return min(myD, key=myD.get)


# print(solution([4, 2, 2, 5, 1, 5, 8]))
# print(solution([1, 2, 3, 4]))
# print(solution([4, 3, 2, 1]))
# print(solution([0, 0, 0, 0]))
print(solution([int(random.choice(string.digits)) for _ in range(100000)]))
