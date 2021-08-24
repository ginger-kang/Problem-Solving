import sys

input = sys.stdin.readline


def is_valid(x, y):
    num_list = []
    for i in range(9):
        num_list.append(board[i][x])
        num_list.append(board[y][i])

    x = x // 3 * 3
    y = y // 3 * 3
    for i in range(y, y + 3):
        for j in range(x, x + 3):
            num_list.append(board[i][j])

    num_set = list(set(num_list))

    rtn = []
    for i in range(1, 10):
        if not i in num_set:
            rtn.append(i)

    return rtn


def dfs(i):
    if i == len(empty):
        for row in board:
            print(*row)
        sys.exit()

    y, x = empty[i]
    nums = is_valid(x, y)

    for num in nums:
        board[y][x] = num
        dfs(i + 1)
        board[y][x] = 0


board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

empty = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            empty.append([i, j])

dfs(0)
