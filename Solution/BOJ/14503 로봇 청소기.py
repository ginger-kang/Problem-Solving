from collections import deque

#북동남서
dx = [-1,0,1,0]
dy = [0,1,0,-1]
tc = 0

def count(maps):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                cnt += 1

    return cnt

def clean(x,y,d,tc):
    while True:
        if tc == 4:
            backX = x - dx[d]
            backY = y - dy[d]

            if maps[backX][backY] == 1:
                print(count(maps))
                return
            else:
                x, y, d, tc = backX, backY, d, 0
                
        #1.
        if maps[x][y] == 0:
            maps[x][y] = 2

        #2. 왼쪽으로 방향이동 후 탐색
        lt = turn(d)
        nx = x + dx[lt]
        ny = y + dy[lt]

        if maps[nx][ny] == 0:
            x, y, d, tc = nx, ny, lt, 0
        else:
            x, y, d, tc = x, y, lt, tc+1

            

def turn(dic):
    if dic == 0:
        return 3
    else:
        return dic-1
    
n, m = map(int, input().split(' '))
r, c, d = list(map(int, input().split(' ')))
maps = [list(map(int, input().split(' '))) for _ in range(n)]

clean(r,c,d,tc)



