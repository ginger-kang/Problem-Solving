n = int(input())
p = []
for _ in range(n):
    input_data = int(input())
    p.append(input_data)

dp = [0]*n
dp[0] = p[0]
dp[1] = dp[0] + p[1]
dp[2] = max(dp[1]+p[2], dp[0]+p[2])

for i in range(3, n):
    dp[i] = max(p[i-1]+p[i]+dp[i-3], dp[i-2]+p[i])

print(dp[n-1])
