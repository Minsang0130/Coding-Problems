def solution(emergency):
    sort_emergency = sorted(emergency)
    result = []
    for num in emergency:
        result.append(len(emergency) - sort_emergency.index(num))
    return result