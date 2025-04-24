def solution(common):
    # 등차인지 확인: 앞 두 항의 차가 다음 두 항의 차와 같으면 등차수열
    if common[1] - common[0] == common[2] - common[1]:
        d = common[1] - common[0]  # 공차
        return common[-1] + d
    else:
        r = common[1] // common[0]  # 공비
        return common[-1] * r