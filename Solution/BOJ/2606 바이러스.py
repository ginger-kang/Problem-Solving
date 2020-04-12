cp = int(input())
n = int(input())
arr = [[] for _ in range(cp + 1)]
visited = [0] * (cp + 1)
cnt = 0

for _ in range(n):
    x, y = map(int, input().split(' '))
    arr[x].append(y)
    arr[y].append(x)

def dfs(v):
    visited[v] = 1
    for e in arr[v]:
        if visited[e] == 0:
            dfs(e)
    
dfs(1)
print(sum(visited)-1)
