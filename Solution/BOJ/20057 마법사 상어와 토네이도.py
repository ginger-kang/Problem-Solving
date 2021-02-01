import math

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = []
posX = n//2
posY = n//2
dist = 1
direction = 0
line_count = 0
block_count = 0
ans = 0

def tornado():
    global posX, posY, direction, block_count, line_count, dist
    nx = posX + dx[direction]
    ny = posY + dy[direction]
    
    spread_sand(nx, ny)
    block_count += 1
    if block_count == dist:
        # 방향 전환
        direction += 1
        direction %= 4
        block_count = 0
        line_count += 1
    if line_count == 2:
        # 길이 + 1
        dist += 1
        line_count = 0

    posX = nx
    posY = ny

def check_out(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def spread_sand(nx, ny):
    global ans, posX, posY
    y = board[ny][nx]
    w1 = math.floor(y * 0.01)
    w2 = math.floor(y * 0.02)
    w5 = math.floor(y * 0.05)
    w7 = math.floor(y * 0.07)
    w10 = math.floor(y * 0.1)
    a = y - 2 * (w1+w2+w7+w10) - w5
    if direction == 0 or direction == 2:
        # 1%
        if check_out(posX, posY - 1):
            board[posY-1][posX] += w1
        else:
            ans += w1
        if check_out(posX, posY + 1):
            board[posY+1][posX] += w1
        else:
            ans += w1
        # 7%
        if check_out(nx, ny - 1):
            board[ny-1][nx] += w7
        else:
            ans += w7
        if check_out(nx, ny + 1):
            board[ny+1][nx] += w7
        else:
            ans += w7
        # 10%
        if check_out(nx + dx[direction], ny - 1):
            board[ny-1][nx+dx[direction]] += w10
        else:
            ans += w10
        if check_out(nx + dx[direction], ny + 1):
            board[ny+1][nx+dx[direction]] += w10
        else:
            ans += w10
        # 2%
        if check_out(nx, ny - 2):
            board[ny-2][nx] += w2
        else:
            ans += w2
        if check_out(nx, ny + 2):
            board[ny+2][nx] += w2
        else:
            ans += w2
        # 5%
        if check_out(nx + dx[direction] * 2, ny):
            board[ny][nx + dx[direction] * 2] += w5
        else:
            ans += w5
        # a
        if check_out(nx + dx[direction], ny):
            board[ny][nx+dx[direction]] += a
        else:
            ans += a
    else:
        # 1%
        if check_out(posX - 1, posY):
            board[posY][posX-1] += w1
        else:
            ans += w1
        if check_out(posX + 1, posY):
            board[posY][posX+1] += w1
        else:
            ans += w1
        # 7%
        if check_out(nx-1, ny):
            board[ny][nx-1] += w7
        else:
            ans += w7
        if check_out(nx+1, ny):
            board[ny][nx+1] += w7
        else:
            ans += w7
        # 10%
        if check_out(nx-1, ny + dy[direction]):
            board[ny+dy[direction]][nx-1] += w10
        else:
            ans += w10
        if check_out(nx+1, ny + dy[direction]):
            board[ny+dy[direction]][nx+1] += w10
        else:
            ans += w10
        # 2%
        if check_out(nx - 2, ny):
            board[ny][nx-2] += w2
        else:
            ans += w2
        if check_out(nx + 2, ny):
            board[ny][nx+2] += w2
        else:
            ans += w2
        # 5%
        if check_out(nx, ny + dy[direction] * 2):
            board[ny+dy[direction]*2][nx] += w5
        else:
            ans += w5
        # a
        if check_out(nx, ny + dy[direction]):
            board[ny+dy[direction]][nx] += a
        else:
            ans += a

for _ in range(n):
    data = list(map(int, input().split(' ')))
    board.append(data)

while True:
    if posX == 0 and posY == 0:
        break
    tornado()

print(ans)
