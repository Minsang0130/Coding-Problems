def solution(n):
    pizza = 1
    while 6*pizza % n != 0:
        pizza += 1
    return pizza