def dfs(i, result):
    global ans
    
    if i >= n:
        return
    if result + arr[i] == s:
        ans += 1

    dfs(i+1, result + arr[i])
    dfs(i+1, result)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

dfs(0, 0)
print(ans)
