from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def snake():
    x, y = 1, 1
    direction = 0
    time = 0
    q = deque()
    q.append([x, y])
    turn_index = 0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if nx >= 1 and nx <= n and ny >= 1 and ny <= n and not [nx, ny] in q:
            # 사과가 있을 경우
            if board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append([nx, ny])
            # 사과가 없을 경우
            else:
                q.append([nx, ny])
                q.popleft()
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny
        if turn_index < l and time == turn[turn_index][0]:
            direction = rotation_snake(direction, turn[turn_index][1])
            turn_index += 1
    return time
            
def rotation_snake(direction, turn):
    if turn == 'D':
        return (direction + 1) % 4
    else:
        return (direction + 3) % 4

n = int(input())
k = int(input())
board = [[0] * (n+1) for _ in range(n+1)]
apples = []
for _ in range(k):
    data = list(map(int, input().split()))
    apples.append(data)

for apple in apples:
    y, x = apple
    board[y][x] = 1

l = int(input())
turn = []
for _ in range(l):
    x, c = input().split()
    turn.append((int(x), c))

print(snake())
