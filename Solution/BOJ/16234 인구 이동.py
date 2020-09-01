from collections import deque
import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    people = board[x][y]
    count = 1
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    union = []
    union.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if l <= abs(board[nx][ny] - board[x][y]) <= r:
                if visited[nx][ny] == 0:
                    people += board[nx][ny]
                    count += 1
                    q.append((nx,ny))
                    union.append((nx, ny))
                    visited[nx][ny] = 1
                    
    for i, j in union:
        board[i][j] = people // count

n, l, r = map(int, input().split(' '))
board = []
for _ in range(n):
    data = list(map(int, input().split(' ')))
    board.append(data)

ans = 0
while True:
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)
                cnt += 1
    if cnt == n * n:
        break
    ans += 1
    
print(ans)
