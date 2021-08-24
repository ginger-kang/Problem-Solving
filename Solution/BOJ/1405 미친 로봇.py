dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, percentage):
    global ans
    if cnt == n:
        ans += percentage
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= (2*n+1) or ny < 0 or ny >= (2*n+1):
            continue
        if board[ny][nx] == 1:
            continue
        board[ny][nx] = 1
        dfs(nx, ny, cnt+1, percentage * per[i] * 0.01)
        board[ny][nx] = 0

input_data = list(map(int, input().split()))
n = input_data[0]
per = input_data[1:]

board = [[0] * (2*n+1) for _ in range(2*n+1)]
board[n][n] = 1

ans = 0
dfs(n, n, 0, 1)
print(ans)
