def solution(dots):
    from itertools import combinations

    def is_parallel(p1, p2, p3, p4):
        return (p2[1] - p1[1]) * (p4[0] - p3[0]) == (p4[1] - p3[1]) * (p2[0] - p1[0])

    return 1 if (
        is_parallel(dots[0], dots[1], dots[2], dots[3]) or
        is_parallel(dots[0], dots[2], dots[1], dots[3]) or
        is_parallel(dots[0], dots[3], dots[1], dots[2])
    ) else 0
