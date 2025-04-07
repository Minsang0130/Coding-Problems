def solution(keyinput, board):
    # 현재 위치
    x, y = 0, 0

    # 좌우 이동 범위: -(가로 // 2) ~ (가로 // 2)
    x_limit = board[0] // 2
    y_limit = board[1] // 2

    # 방향별 이동
    for key in keyinput:
        if key == "up" and y < y_limit:
            y += 1
        elif key == "down" and y > -y_limit:
            y -= 1
        elif key == "left" and x > -x_limit:
            x -= 1
        elif key == "right" and x < x_limit:
            x += 1

    return [x, y]
