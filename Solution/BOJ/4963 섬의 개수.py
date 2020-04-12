from collections import deque

while True:
    w, h = map(int, input().split(' '))

    if not w and not h:
        break

    m = [list(map(int, input().split(' '))) for _ in range(h)]
    check = [[False]*w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and check[i][j] == False:
                check[i][j] = True
                cnt += 1
                q = deque()
                q.append((i, j))

                while q:
                    x, y = q.popleft()
                    for dx, dy in (1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1):
                        nx, ny = x+dx, y+dy
                        if nx < 0 or nx >= h or ny < 0 or ny >= w:
                            continue
                        if m[nx][ny] == 1 and check[nx][ny] == False:
                            check[nx][ny] = True
                            q.append((nx,ny))
    print(cnt)
                        
            
    
