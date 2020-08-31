import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
result = 0
for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        result += 1
        
print(result)
