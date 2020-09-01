import sys
input = sys.stdin.readline

n, m = map(int, input().split(' '))
board = []
for _ in range(n):
    data = list(map(int, input().split(' ')))
    board.append(data)

pre_sum = [[0] for _ in range(n)]
for i in range(n):
    sum_value = 0
    for j in range(n):
        sum_value += board[i][j]
        pre_sum[i].append(sum_value)

#print(pre_sum)
        
for _ in range(m):
    x1, y1, x2, y2 = list(map(int, input().split(' ')))
    result = 0
    for i in range(x1-1, x2):
        result += pre_sum[i][y2] - pre_sum[i][y1-1]
    print(result)
