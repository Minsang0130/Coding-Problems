def solution(n, slicer, num_list):
    a, b, c = slicer
    if n == 1:
        return num_list[0:b+1]
    if n == 2:
        return num_list[a:]
    if n == 3:
        return num_list[a:b+1]
    if n == 4:
        return num_list[a:b+1:c]