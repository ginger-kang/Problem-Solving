import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def bfs(y, x):
    q = deque()
    q.append([x, y])
    visited[y][x] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            while True:
                if nx < 0 or nx >= w or ny < 0 or ny >= h or board[ny][nx] == '*':
                    break
                if visited[ny][nx] < visited[y][x] + 1:
                    break
                visited[ny][nx] = visited[y][x] + 1
                q.append([nx, ny])
                nx = nx + dx[i]
                ny = ny + dy[i]

w, h = map(int, input().split())
board = []
for _ in range(h):
    board.append(input())

visited = [[INF] * w for _ in range(h)]

C = []
for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            C.append([i, j])

start = C[0]
end = C[1]
bfs(start[0], start[1])
print(visited[end[0]][end[1]] - 1)
