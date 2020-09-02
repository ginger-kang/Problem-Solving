# 위 앞 바닥 뒤 동 서
dice = [0,0,0,0,0,0]

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(order):
    global dice, current_pos
    x, y = current_pos[0], current_pos[1]
    nx = x + dx[order-1]
    ny = y + dy[order-1]
    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        return
    rotation(order)
    if board[nx][ny] == 0:
        board[nx][ny] = dice[2]
    else:
        dice[2] = board[nx][ny]
        board[nx][ny] = 0
    current_pos = (nx, ny)
    print(dice[0])
    return

def rotation(order):
    global dice
    if order == 1:
        dice[4], dice[2], dice[5], dice[0] = dice[0], dice[4], dice[2], dice[5]
    elif order == 2:
        dice[5], dice[0], dice[4], dice[2] = dice[0], dice[4], dice[2], dice[5]
    elif order == 3:
        dice[2], dice[1], dice[0], dice[3] = dice[3], dice[2], dice[1], dice[0]
    elif order == 4:
        dice[0], dice[1], dice[2], dice[3] = dice[3], dice[0], dice[1], dice[2]
    return    

n, m, x, y, k = list(map(int, input().split(' ')))
board = []
for _ in range(n):
    data = list(map(int, input().split(' ')))
    board.append(data)
order = list(map(int, input().split(' ')))
current_pos = (x,y)

for k in order:
    move(k)

