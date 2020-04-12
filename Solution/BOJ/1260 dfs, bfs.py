N, M, V = map(int, input().split(' '))
maps = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    link = list(map(int, input().split(' ')))
    maps[link[0]][link[1]] = 1
    maps[link[1]][link[0]] = 1

def dfs(V, maps, visited):
    visited += [V]
    for i in range(len(maps[V])):
        if maps[V][i] and i not in visited:
            visited = dfs(i, maps, visited)

    return visited

def bfs(V):
    q = [V]
    visited = [V]
    while q:
        current_node = q.pop(0)
        for i in range(len(maps[current_node])):
            if maps[current_node][i] and i not in visited:
                visited += [i]
                q += [i]

    return visited

print(*dfs(V, maps, []))
print(*bfs(V))
