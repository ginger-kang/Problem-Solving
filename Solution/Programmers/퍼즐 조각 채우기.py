from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
puzzle = {}
result = 0


def rotation(board):
    n = len(board)
    m = len(board[0])
    rtn = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rtn[j][n - 1 - i] = board[i][j]

    return rtn


def check(cnt, parsed):
    global puzzle

    if puzzle.get(cnt) is None:
        return

    boards = puzzle[cnt]
    for board in boards:
        remove_target = board
        for _ in range(4):
            if board == parsed:
                puzzle[cnt].remove(remove_target)
                return True
            board = rotation(board)

    return False


def parse_block(n, visited, board, cnt, flag):
    global result

    x1, x2, y1, y2 = n, 0, n, 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                x1 = min(x1, j)
                x2 = max(x2, j)
                y1 = min(y1, i)
                y2 = max(y2, i)

    parsed = []
    for i in range(y1, y2 + 1):
        temp = []
        for j in range(x1, x2 + 1):
            if board[i][j] == 2:
                temp.append(1)
            else:
                temp.append(0)
        parsed.append(temp)

    if flag:
        set_puzzle(parsed, cnt)
    else:
        if check(cnt, parsed):
            result += cnt
        return


def set_puzzle(parsed, cnt):
    global puzzle

    if puzzle.get(cnt) is not None:
        puzzle[cnt].append(parsed)
    else:
        puzzle[cnt] = [parsed]


def bfs(n, start, board, flag):
    q = deque()
    q.append(start)
    visited = [[False] * n for _ in range(n)]
    board[start[0]][start[1]] = 2
    visited[start[0]][start[1]] = True
    cnt = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[ny][nx]:
                continue
            if flag and board[ny][nx]:
                continue
            if not flag and not board[ny][nx]:
                continue
            board[ny][nx] = 2
            visited[ny][nx] = True
            cnt += 1
            q.append([ny, nx])

    parse_block(n, visited, board, cnt, flag)


def solution(game_board, table):
    global puzzle

    n = len(game_board)
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                bfs(n, [i, j], game_board, True)

    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                bfs(n, [i, j], table, False)

    return result
