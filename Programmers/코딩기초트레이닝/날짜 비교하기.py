def solution(date1, date2):
    for idx in range(len(date1)):
        if date1[idx] > date2[idx]:
            return 0
        elif date1[idx] < date2[idx]:
            return 1
    return 0ㅎ