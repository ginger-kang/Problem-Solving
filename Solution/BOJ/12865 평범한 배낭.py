n, k = map(int, input().split())
w = [0]
v = [0]
for _ in range(n):
    input_data = list(map(int, input().split()))
    w.append(input_data[0])
    v.append(input_data[1])

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(k, 0, -1):
        if j - w[i] >= 0:
            dp[i][j] = max(dp[i-1][j], v[i] + dp[i-1][j-w[i]])
        else:
            dp[i][j] = dp[i-1][j]
            
print(max(dp[n]))
