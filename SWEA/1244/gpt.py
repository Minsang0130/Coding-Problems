def dfs(num_list, k, max_num):
    # 종료 조건: 교환 횟수를 모두 사용한 경우
    if k == 0:
        return int("".join(num_list))

    # 현재 숫자를 튜플로 저장해 방문 체크
    key = (tuple(num_list), k)
    if key in visited:
        return max_num
    gvb
    visited.add(key)
    
    n = len(num_list)
    for i in range(n):
        for j in range(i + 1, n):
            # i와 j를 교환
            num_list[i], num_list[j] = num_list[j], num_list[i]
            
            # 재귀 호출을 통해 다음 교환을 수행
            max_num = max(max_num, dfs(num_list, k - 1, max_num))
            
            # 교환을 원래 상태로 되돌림
            num_list[i], num_list[j] = num_list[j], num_list[i]

    return max_num

# 테스트 케이스 처리
T = int(input())

for tc in range(1, T + 1):
    num, k = input().split()
    k = int(k)
    num_list = list(num)
    visited = set()
    
    result = dfs(num_list, k, 0)
    print(f"#{tc} {result}")
