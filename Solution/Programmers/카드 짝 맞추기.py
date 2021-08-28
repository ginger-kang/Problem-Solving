import itertools
import copy
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def distance(start, board):
    q = deque()
    q.append(start)
    dist = [[0] * 4 for _ in range(4)]
    visited = [[False] * 4 for _ in range(4)]
    visited[start[0]][start[1]] = True
    while q:
        y, x = q.popleft()
        for i in range(4):
            ctrl = 1
            while True:
                nx = x + dx[i] * ctrl
                ny = y + dy[i] * ctrl
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                    ctrl -= 1
                    break
                if board[ny][nx]:
                    break
                ctrl += 1
            for j in [1, ctrl]:
                nx = x + dx[i] * j
                ny = y + dy[i] * j
                if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or visited[ny][nx]:
                    continue
                dist[ny][nx] = dist[y][x] + 1
                visited[ny][nx] = True
                q.append([ny, nx])

    return dist


def solution(board, r, c):
    card_cnt = 0
    card_info = {}
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                card_cnt = max(card_cnt, board[i][j])
                if card_info.get(board[i][j]) is not None:
                    card_info[board[i][j]].append((i, j))
                else:
                    card_info[board[i][j]] = [(i, j)]

    card_case = list(itertools.permutations(range(1, card_cnt + 1), card_cnt))
    ans = int(1e9)
    for case in card_case:
        curr_pos = [r, c]
        copy_board = copy.deepcopy(board)
        result = 0
        for card in case:
            tmp = [0, 0]
            for i in range(2):
                dist = distance(curr_pos, copy_board)
                tmp[i] = dist[card_info[card][i][0]][card_info[card][i][1]]
            for i in range(2):
                curr_pos = card_info[card][i]
                dist = distance(curr_pos, copy_board)
                tmp[i] += dist[card_info[card][(i + 1) % 2][0]][
                    card_info[card][(i + 1) % 2][1]
                ]
            if tmp[0] < tmp[1]:
                curr_pos = card_info[card][1]
                result += tmp[0] + 2
            else:
                curr_pos = card_info[card][0]
                result += tmp[1] + 2
            a, b = card_info[card][0], card_info[card][1]
            copy_board[a[0]][a[1]] = 0
            copy_board[b[0]][b[1]] = 0
        ans = min(ans, result)

    return ans
