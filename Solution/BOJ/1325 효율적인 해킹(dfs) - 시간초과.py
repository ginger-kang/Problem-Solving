import sys
sys.setrecursionlimit(100000)

def dfs(v, visited):
    visited[v] = 1
    for e in arr[v]:
        if visited[e] == 0:
            dfs(e, visited)

    return sum(visited)

n, m = map(int, input().split(' '))
arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split(' '))
    #arr[x].append(y)
    arr[y].append(x)

result = [0]
for i in range(n):
    visited = [0] * (n+1)
    result.append(dfs(i+1, visited))

for i in range(len(result)):
    if result[i] == max(result):
        print(i, end = ' ')
