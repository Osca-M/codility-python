def solution(N: int) -> int:
    return len(max(format(N, 'b').strip('0').split('1')))
