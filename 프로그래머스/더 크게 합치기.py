import sys
def solution(a,b):
    return int(max(f"{a}{b}", f"{b}{a}"))

print(solution(1,43))