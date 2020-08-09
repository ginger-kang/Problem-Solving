from collections import deque

# 동남서북
dx = [1, 0, -1, 0] # r
dy = [0, 1, 0, -1] # c

def dummy(board, change_dir):
    snake_head = (1,1)
    direction = 0
    time = 0
    board[snake_head[0]][snake_head[1]] = 2
    # (c, r)
    q = deque()
    q.append(snake_head)
    while True:
        #print(q, time, direction)
        nx = snake_head[1] + dx[direction]
        ny = snake_head[0] + dy[direction]
        if nx >= 1 and ny >= 1 and nx <= n and ny <= n and board[ny][nx] != 2:
            # 사과가 없을 경우
            if board[ny][nx] == 0:
                snake_head = (ny, nx)
                board[ny][nx] = 2
                q.append(snake_head)
                y,x = q.popleft()
                board[y][x] = 0
            # 사과가 있을 경우
            else:
                snake_head = (ny, nx)
                board[ny][nx] = 2
                q.append(snake_head)
            time += 1
            for i in change_dir:
                if time == i[0]:
                    direction = turn(direction, i[1])
        else:
            print(time+1)
            break
        
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
        
    return direction

n = int(input())
k = int(input())

# (c, r)
apple = []
for i in range(k):
    input_data = list(map(int, input().split(' ')))
    apple.append(input_data)
    
l = int(input())

change_dir = []
for i in range(l):
    input_data = input().split(' ')
    change_dir.append((int(input_data[0]), input_data[1]))

board = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(n+1):
        if [i, j] in apple:
            board[i][j] = 1
            
dummy(board, change_dir)
