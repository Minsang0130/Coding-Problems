dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution(n):
    arr = [[False] * n for _ in range(n)]
    count = 1
    cx, cy = 0, 0
    # dxy의 인덱스
    d_idx = 0
    while True:
        arr[cx][cy] = count

        if count == n * n:
            break
        while True:
            # 다음 방향 이동
            nx, ny = cx + dxy[d_idx][0], cy + dxy[d_idx][1]
            # 다음 값이 범위를 넘으면
            if nx < 0 or nx >=n or ny < 0 or ny >=n:
                d_idx = (d_idx + 1) % 4
            # 이미 지나온 길이면
            elif arr[nx][ny]:
                d_idx = (d_idx + 1) % 4
            else:
                cx, cy = nx, ny
                break

        count += 1

    return arr

print(solution(4))
