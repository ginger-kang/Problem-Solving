from collections import deque


def find_max_weight(start, target):
    q = deque()
    q.append(start)
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        curr = q.popleft()
        for i in graph[curr]:
            node, weight = i
            if weight >= target and not visited[node]:
                visited[node] = True
                q.append(node)

    if visited[y]:
        return True
    else:
        return False


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
x, y = map(int, input().split())

left = 1
right = 1000000000
ans = 0
while left <= right:
    mid = (left + right) // 2
    if find_max_weight(x, mid):
        left = mid + 1
        ans = mid
    else:
        right = mid - 1

print(ans)
