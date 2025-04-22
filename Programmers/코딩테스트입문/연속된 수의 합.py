def solution(num, total):
    num_list = []
    start = -100
    while True:
        num_list = list(range(start, start + num))
        num_sum = sum(num_list)
        if num_sum == total:
            break
        start += 1
    return num_list