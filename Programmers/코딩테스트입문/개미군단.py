def solution(hp):
    result = 0
    ant_list = [5, 3, 1]
    for ant in ant_list:
        if hp == 0:
            break
        result += hp // ant
        hp = hp % ant
    return result