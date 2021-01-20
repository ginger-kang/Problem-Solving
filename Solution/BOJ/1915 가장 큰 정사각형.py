n, m = map(int, input().split(' '))
board = []
for i in range(n):
    tmp = input()
    board.append(list(map(int, list(tmp))))

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i-1][j-1] == 1:
            minVal = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
            dp[i][j] = minVal + 1
            ans = max(ans, dp[i][j])

print(ans * ans)
