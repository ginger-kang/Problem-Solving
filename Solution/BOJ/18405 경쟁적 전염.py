from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(virus):
    q = deque(virus)
    while q:
        tv, tt, tx, ty = q.popleft()
        if tt == s:
            break
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] = tv
                    q.append((tv, tt+1, nx, ny))

n, k = map(int, input().split(' '))
board = []
virus = []
for i in range(n):
    data = list(map(int, input().split(' ')))
    board.append(data)
    for j in range(n):
        if board[i][j] != 0:
            virus.append((board[i][j], 0, i, j))

virus.sort()

s, x, y = map(int, input().split(' '))

bfs(virus)
#print(board)
print(board[x-1][y-1])

