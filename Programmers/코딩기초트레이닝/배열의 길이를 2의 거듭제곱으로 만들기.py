def solution(arr):
    arr_len = len(arr)
    i = 1
    pow_num = 1
    while pow_num < arr_len:
        pow_num = pow(2, i)
        i += 1

    if len(arr) != pow_num:
        while len(arr) != pow_num:
            arr.append(0)

    return arr