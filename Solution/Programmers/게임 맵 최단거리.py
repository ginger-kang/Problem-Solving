from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(dist, n, m, maps):
    q = deque()
    dist[0][0] = 1
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or not maps[ny][nx] or dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[-1] * m for _ in range(n)]
    bfs(dist, n, m, maps)
    
    return dist[n-1][m-1]