from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#baby_shark(level, position, count)

def eat(pos):
    global answer, baby_shark, space
    bsp = baby_shark[1]
    q = deque()
    q.append(bsp)
    visited = [[False] * n for _ in range(n)]
    visited[bsp[1]][bsp[0]] = True
    distance = 0
    state = False
    eatable = []
    
    while q:
        distance += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if space[ny][nx] <= baby_shark[0] and visited[ny][nx] == False:
                    visited[ny][nx] = True
                    if 0 < space[ny][nx] < baby_shark[0]:
                        eatable.append((nx, ny))
                        state = True
                    else:
                        q.append((nx,ny))
        if eatable:
            break

    if eatable:
        eatable = sorted(eatable, key = lambda x:(x[1],x[0]))
        space[eatable[0][1]][eatable[0][0]] = 9
        space[bsp[1]][bsp[0]] = 0
        baby_shark[1] = eatable[0]
        baby_shark[2] -= 1
        if baby_shark[2] == 0:
            baby_shark[0] += 1
            baby_shark[2] = baby_shark[0]
        answer += distance
        return True
    else:
        return False
        
        

n = int(input())
answer = 0
space = []
eatable = []

for _ in range(n):
    space.append(list(map(int, input().split(' '))))

baby_shark = [2, (0,0), 2]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            baby_shark[1] = (j,i)
            pos = (j, i)
            space[i][j] = 0
            break

while True:
    if not eat(pos):
        break

print(answer)
