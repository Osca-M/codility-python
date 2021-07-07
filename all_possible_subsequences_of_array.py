# print all possible subsequences for given array using recursion
def solution(a: list, index: int, sub_array: list):
    if index == len(a):
        if len(sub_array) != 0:
            print(sub_array)
    else:
        solution(a, index + 1, sub_array)
        solution(a, index + 1, sub_array + [a[index]])
    return


