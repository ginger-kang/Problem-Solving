from collections import deque

n = int(input())

paint = [input() for _ in range(n)]
check = [[False]*n for _ in range(n)]
check_2 = [[False]*n for _ in range(n)]
cnt_1 = 0
cnt_2 = 0

def bfs(i, j, check):
    q = deque()
    check[i][j] = True
    q.append((i,j))
    current_color = paint[i][j]
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if current_color == paint[nx][ny] and check[nx][ny] == False:
                check[nx][ny] = True
                q.append((nx,ny))

def bfs2(i, j, check):
    q = deque()
    check[i][j] = True
    q.append((i,j))
    f = {
        'R' : 'R',
        'G' : 'R',
        'B' : 'B'
    }
    current_color = f[paint[i][j]]
    while q:
        x, y = q.popleft()
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if current_color == f[paint[nx][ny]] and check[nx][ny] == False:
                check[nx][ny] = True
                q.append((nx,ny))


for i in range(n):
    for j in range(n):
        if check[i][j] == False:
            bfs(i, j, check)
            cnt_1 += 1
            
for i in range(n):
    for j in range(n):
        if check_2[i][j] == False:
            bfs2(i, j, check_2)
            cnt_2 += 1
    
print(cnt_1, cnt_2)
            
            
        
