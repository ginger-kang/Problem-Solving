from collections import deque

n = int(input())

danji = [input() for _ in range(n)]
check = [[False]*n for _ in range(n)]

q = deque()
cnt = 0
result = []
for i in range(n):
    for j in range(n):
        if danji[i][j] == '1' and check[i][j] == False:
            check[i][j] = True
            q.append((i, j))
            cnt += 1
            area = 1
            while q:
                x, y = q.popleft()
                for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
                    nx, ny = x+dx, y+dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if danji[nx][ny] == '1' and check[nx][ny] == False:
                        check[nx][ny] = True
                        area += 1
                        q.append((nx,ny))
            result.append(area)
print(cnt)

result = sorted(result)
for i in result:
    print(i, end = '\n')
        
                    
                
