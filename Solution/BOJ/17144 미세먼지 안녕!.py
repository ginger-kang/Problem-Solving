from collections import deque
import copy 

def munji(m, k):
    after_munji = copy.deepcopy(m)
    if k == t:
        ans = 0
        for i in range(r):
            ans += sum(after_munji[i])
        print(ans+2)
        return
    
    q = deque()
    for i in range(r):
        for j in range(c):
            if m[i][j] > 0:
                q.append((i,j))
    
    while q:
        y, x = q.popleft()
        cnt = 0
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= c or ny < 0 or ny >= r:
                continue
            if m[ny][nx] != -1:
                after_munji[ny][nx] += m[y][x]//5
                cnt += 1
        after_munji[y][x] -= ((m[y][x]//5) * cnt)            
    
    cn = []
    for i in range(r):
        if m[i][0] == -1:
            cn.append(i)

    tmp = [after_munji[cn[0]][1]]
    after_munji[cn[0]][1] = 0
    for i in range(2,c-1):
        tmp.append(after_munji[cn[0]][i])
        after_munji[cn[0]][i] = tmp.pop(0)
    for i in range(cn[0], -1, -1):
        tmp.append(after_munji[i][c-1])
        after_munji[i][c-1] = tmp.pop(0)
    for i in range(c-2, -1, -1):
        tmp.append(after_munji[0][i])
        after_munji[0][i] = tmp.pop(0)
    for i in range(1, cn[0]):
        tmp.append(after_munji[i][0])
        after_munji[i][0] = tmp.pop(0)
    
    tmp = [after_munji[cn[1]][1]]
    after_munji[cn[1]][1] = 0
    for i in range(2,c-1):
        tmp.append(after_munji[cn[1]][i])
        after_munji[cn[1]][i] = tmp.pop(0)
    for i in range(cn[1], r):
        tmp.append(after_munji[i][c-1])
        after_munji[i][c-1] = tmp.pop(0)
    for i in range(c-2, -1, -1):
        tmp.append(after_munji[r-1][i])
        after_munji[r-1][i] = tmp.pop(0)
    for i in range(r-2, cn[1], -1):
        tmp.append(after_munji[i][0])
        after_munji[i][0] = tmp.pop(0)
    
    munji(after_munji,k+1)

r, c, t = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(r)]
after_munji = copy.deepcopy(maps)

munji(maps,0)
