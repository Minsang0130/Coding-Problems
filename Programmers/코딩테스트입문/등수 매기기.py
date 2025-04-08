def solution(score):
    n = len(score)
    # 각 학생의 평균을 계산
    averages = [ (s[0] + s[1]) / 2 for s in score ]
    
    answer = []
    for i in range(n):
        rank = 1  # 자신보다 높은 평균을 가진 학생 수에 1을 더한 것이 등수.
        for j in range(n):
            if averages[j] > averages[i]:
                rank += 1
        answer.append(rank)
        
    return answer