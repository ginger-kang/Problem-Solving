from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

def bfs(v):
    q = deque()
    q.append(v)
    cnt = 0
    ap[v] = 1
    while q:
        v = q.popleft()
        for e in arr[v]:
            if ap[e] == 0:
                ap[e] = 1
                cnt += 1
                q.append(e)

    return cnt

for _ in range(t):
    n, m = map(int, input().split(' '))
    arr = [[] for _ in range(n+1)]
    ap = [0] * (n+1)

    for _ in range(m):
        x, y = map(int, input().split(' '))
        arr[x].append(y)
        arr[y].append(x)

    result = 0
    for i in range(n+1):
        if ap[i] == 0:
            result += bfs(i)

    print(result)
