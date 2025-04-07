def solution(lines):
    offset = 100  
    coverage = [0] * 201
    
    # 각 선분에 대하여 해당하는 구간의 카운트 증가
    for start, end in lines:
        # 선분 [start, end]는 정수 구간 start부터 end-1까지를 덮습니다.
        for i in range(start, end):
            coverage[i + offset] += 1
    
    # 2개 이상의 선분이 겹치는 구간의 길이를 합산
    answer = 0
    for cnt in coverage:
        if cnt >= 2:
            answer += 1
            
    return answer
