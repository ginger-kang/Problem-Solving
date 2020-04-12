n = int(input())
arr = list(map(int, input().split(' ')))

dp = []
dp.append(1)
for i in range(1, n):
    dp.append(1)
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
