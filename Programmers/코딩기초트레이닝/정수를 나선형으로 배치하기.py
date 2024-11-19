dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))  # Directions: Right, Up, Left, Down


def solution(n):
    def dfs(cx, cy, count):
        if count == n * n:  # Stop when all cells are filled
            return True  # Base case: the grid is completely filled

        arr[cx][cy] = count

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:  # Ensure within bounds
                continue

            if arr[nx][ny] != -1:  # Cell is already filled
                continue

            if dfs(nx, ny, count + 1):  # Recursive call with updated count
                return True

        return False  # Return False if no further moves are possible (backtrack)

    arr = [[-1] * n for _ in range(n)]  # Initialize grid with -1 (unvisited cells)

    dfs(0, 0, 0)  # Start DFS from the top-left corner

    return arr  # Return the filled grid
