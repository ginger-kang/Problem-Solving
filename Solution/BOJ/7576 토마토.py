from collections import deque

def tomato(maps):
    q = deque()
    day = -1
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 1:
                q.append((i,j))
                
    while q:
        day += 1
        for _ in range(len(q)):
            x, y = q.popleft()

            for dx, dy in (-1,0), (1,0), (0,-1), (0,1):
                nx, ny = x+dx, y+dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == 0:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                return -1       
    
    return day

if __name__ == "__main__":
    m, n = map(int, input().split(' '))
    maps = [list(map(int, input().split(' '))) for _ in range(n)]
    
    print(tomato(maps))
