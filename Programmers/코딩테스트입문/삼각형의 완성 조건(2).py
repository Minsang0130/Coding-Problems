def solution(sides):
    a, b = sides
    return min(a, b) + (a + b - 1 - max(a, b))
