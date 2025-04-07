def solution(order):
    result = 0
    order_list = [int(n) for n in str(order)]
    for num in order_list:
        if num % 3 == 0 and num != 0:
            result += 1
    return result