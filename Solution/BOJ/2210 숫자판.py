import sys
sys.setrecursionlimit(100000)

def bt(x, y, tmp):
    if len(tmp) == 6:
        if tmp not in arr:
            arr.append(tmp)
        return
    
    for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < 5 and 0 <= ny < 5:
            bt(nx, ny, tmp + maps[nx][ny])

maps = [list(map(str, input().split(' '))) for _ in range(5)]
arr = []

for i in range(5*5):
    x = i//5
    y = i%5
    bt(x, y, maps[x][y])

print(len(arr))
