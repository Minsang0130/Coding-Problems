def solution(a,b):
    a, b= str(a), str(b)
    c = int(a+b) *2
    return max(f"{a}{b}", str(c))

solution(1,91)