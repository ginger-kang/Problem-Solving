from collections import deque

def bfs(i, j, visited, matrix):
    q = deque()
    q.append((i, j))
    cnt = 0
    visited[i][j] = True
    cnt += 1
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if matrix[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append((nx, ny))

    return cnt
    
for _ in range(int(input())):
    M, N, K = list(map(int, input(). split(' ')))
    matrix = [[0]*M for _ in range(N)]
    for _ in range(K):
        bc = list(map(int, input().split(' ')))
        matrix[bc[1]][bc[0]] = 1
    visited = [[False]*M for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] == False:
                result += bfs(i, j, visited, matrix)

    print(result)
    
