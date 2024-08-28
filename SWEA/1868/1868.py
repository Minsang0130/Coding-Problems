import sys
import pprint
sys.stdin = open('input.txt', 'r')

# 테스트 케이스의 수를 입력받음
T = int(input())

# 8방향을 나타내는 델타 값 설정 (상하좌우 및 대각선 방향)
dxy = [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

# 특정 위치 주변의 지뢰 수를 계산하는 함수
def count_mines(x, y):
    count = 0
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        # 범위를 벗어나지 않고, 해당 위치에 지뢰가 있는 경우 카운트 증가
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == '*':
            count += 1
    return count

# 클릭했을 때 주변의 지뢰 수를 표시하는 함수
def popping(x, y):
    # 이미 숫자가 표시된 칸이나 지뢰가 있는 칸은 건너뜀
    if arr[x][y] != '.':
        return
    
    # 현재 위치의 주변 지뢰 수를 계산
    count = count_mines(x, y)
    # 현재 위치에 지뢰 수를 표시 (지뢰가 없으면 0 표시)
    arr[x][y] = str(count)
    
    # 만약 주변에 지뢰가 없으면 (count == 0), 8방향으로 재귀 호출하여 연쇄적으로 표시
    if count == 0:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                popping(nx, ny)

# 각 테스트 케이스마다 실행
for test_case in range(1, T + 1):
    # 표의 크기 N을 입력받음
    N = int(input())
    # N*N 표의 내용을 2차원 리스트로 입력받음
    arr = [list(input()) for _ in range(N)]
    
    result = 0
    
    # 모든 지점에서 '.'인 칸을 탐색하여 클릭 실행
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                # 만약 해당 위치 주변에 지뢰가 없다면, popping 함수 실행
                if count_mines(i, j) == 0:
                    popping(i, j)
                    result += 1
                
    
    # 아직 남아있는 '.'인 칸들을 모두 카운트
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                result += 1

    # pprint.pprint(arr)
    # 결과 출력 (테스트 케이스 번호와 클릭 횟수)
    print(f'#{test_case} {result}')
