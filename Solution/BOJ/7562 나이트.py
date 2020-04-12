from collections import deque

def bfs(startPointX, startPointY, endPointX, endPointY):
    q = deque()
    q.append((startPointX, startPointY))
    maps[startPointX][startPointY] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in (-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if x == endPointX and y == endPointY:
                return maps[x][y] -1
            if maps[nx][ny] == 0:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                
for _ in range(int(input())):
    l = int(input())
    maps = [[0]*l for _ in range(l)]
    startPointX, startPointY = map(int, input().split(' '))
    endPointX, endPointY = map(int, input().split(' '))

    print(bfs(startPointX, startPointY, endPointX, endPointY))
    
