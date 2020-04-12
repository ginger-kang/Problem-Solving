from collections import deque

m, n, k = list(map(int, input().split(' ')))

sq = [list(map(int, input().split(' '))) for _ in range(k)]
board = [[0]*n for _ in range(m)]

for t in sq:
    for i in range(t[1], t[3]):
        for j in range(t[0], t[2]):
            board[i][j] = 1

def bfs(i, j):
    q = deque()
    q.append((i, j))
    sum = 1
    board[i][j] = -1
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 0:
                sum += 1
                q.append((nx, ny))
                board[nx][ny] = -1
    return sum
                
cnt = 0
tmp = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            tmp.append(bfs(i,j))
            cnt += 1
print(cnt, end = '\n')

tmp = sorted(tmp)
for i in tmp:
    print(i, end = ' ')

        
