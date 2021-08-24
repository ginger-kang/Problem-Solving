def dfs(depth):
    global ans
    if depth == n:
        result = 0
        for i in range(n - 1):
            result += abs(tmp[i + 1] - tmp[i])
        ans = max(ans, result)
        return

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        tmp.append(nums[i])
        dfs(depth + 1)
        tmp.pop()
        visited[i] = 0


n = int(input())
nums = list(map(int, input().split()))
visited = [0] * n
tmp = []
ans = 0
dfs(0)

print(ans)
