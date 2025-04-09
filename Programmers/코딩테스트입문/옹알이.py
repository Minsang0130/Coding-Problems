from itertools import permutations

def solution(babbling):
    # 가능한 네 가지 발음을 미리 정의합니다.
    allowed = ["aya", "ye", "woo", "ma"]
    valid_set = set()
    
    # 1개부터 4개까지 발음을 중복 없이 이어 붙인 모든 경우를 valid_set에 추가합니다.
    for k in range(1, 5):
        for p in permutations(allowed, k):
            valid_set.add("".join(p))
    
    # babbling에 있는 각 문자열이 valid_set에 존재하면 카운트합니다.
    count = sum(1 for word in babbling if word in valid_set)
    return count