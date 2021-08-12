from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    while q:
        curr = q.popleft()
        for i in tree[curr]:
            if parent[i] == 0:
                parent[i] = curr
                q.append(i)

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

bfs()
for i in parent[2:]:
    print(i)
