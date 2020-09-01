dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y, count, total):
    global result
    if count == 4:
        result = max(result, total)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= m or ny >= n:
            continue
        if visited[ny][nx] == 0:
            visited[ny][nx] += 1
            dfs(nx, ny, count+1, total + board[ny][nx])
            visited[ny][nx] -= 1
                     

def tet(x, y):
    global result
    total = board[y][x]
    if x == 0 and y == 0:
        return
    if x == 0 and y == n-1:
        return
    if x == m-1 and y == 0:
        return
    if x == m-1 and y == n-1:
        return
    if y == 0:
        total += board[y][x-1] + board[y][x+1] + board[y+1][x]
    elif y == n-1:
        total += board[y][x-1] + board[y][x+1] + board[y-1][x]
    elif x == 0:
        total += board[y-1][x] + board[y+1][x] + board[y][x+1]
    elif x == m-1:
        total += board[y-1][x] + board[y+1][x] + board[y][x-1]
    else:
        result = max(result, total + board[y][x-1] + board[y][x+1] + board[y+1][x])
        result = max(result, total + board[y][x-1] + board[y][x+1] + board[y-1][x])
        result = max(result, total + board[y-1][x] + board[y+1][x] + board[y][x+1])
        result = max(result, total + board[y-1][x] + board[y+1][x] + board[y][x-1])

    result = max(result, total)

n, m = map(int, input().split(' '))
board = []
result = 0
for _ in range(n):
    data = list(map(int, input().split(' ')))
    board.append(data)

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] += 1
        dfs(j, i, 1, board[i][j])
        visited[i][j] -= 1
        tet(j, i)
print(result)
