from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited = [False] * (n+1)
    visited[v] = True
    count = 1
    while q:
        v = q.popleft()
        for e in arr[v]:
            if visited[e] == False:
                q.append(e)
                visited[e] = True
                count += 1

    return count

n, m = map(int, input().split(' '))
arr = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split(' '))
    #arr[x].append(y)
    arr[y].append(x)

result = []
maxVal = -1
for i in range(1, n+1):
    tmp = bfs(i)
    if tmp > maxVal:
        result = [i]
        maxVal = tmp
    elif tmp == maxVal:
        result.append(i)
        maxVal = tmp

for i in result:
    print(i, end = ' ')
