def solution(board):
    n = len(board)
    # 위험지역 여부를 저장할 2차원 리스트 (False: 안전, True: 위험)
    danger = [[False] * n for _ in range(n)]

    # 지뢰가 있는 칸과 그 주변 8방향을 표시하기 위한 좌표 변화
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 0), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    # board의 각 칸을 순회하면서 지뢰가 있는 경우 주변 8방향 포함 처리
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger[ni][nj] = True

    # 위험지역이 아닌 칸의 개수 세기
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if not danger[i][j]:
                safe_count += 1

    return safe_count
