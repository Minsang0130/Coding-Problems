def solution(order):
    result = 0
    for coffe in order:
        if 'americano' in coffe:
            result += 4500
        elif 'cafelatte' in coffe:
            result += 5000
        else:
            result += 4500
    return result