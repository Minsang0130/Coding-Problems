def solution(money):
    coffe = money // 5500
    return [coffe, money - coffe * 5500]