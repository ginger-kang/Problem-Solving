from collections import deque
import copy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i, j, maps):
    #copy_maps = copy.deepcopy(maps)
    check = [[0]*m for _ in range(n)]

    q = deque()
    q.append((i, j))
    check[i][j] += 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 'L' and check[nx][ny] == 0:
                check[nx][ny] = check[x][y] + 1
                q.append((nx,ny))

    #print(check)
    tmp_max = 0
    for i in check:
        tmp_max = max(tmp_max, max(i))

    return tmp_max-1

if __name__ == '__main__':
    n, m = map(int, input().split(' '))
    maps = [input() for _ in range(n)]

    max_dist = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'L':
                max_dist = max(bfs(i, j, maps), max_dist)

    print(max_dist)


