import sys
from collections import defaultdict

sys.setrecursionlimit(300000)
ans = 0

def dfs(curr, parent, visited, tree, a):
    global ans
    
    # 리프노드에서부터 가중치를 부모에 넘겨줌
    for i in tree[curr]:
        if not visited[i]:
            visited[i] = True
            dfs(i, curr, visited, tree, a)
    
    a[parent] += a[curr]
    ans += abs(a[curr])
    a[curr] = 0

def solution(a, edges):
    global ans
    if sum(a) != 0:
        return -1
    
    tree = defaultdict(list)
    for edge in edges:
        u, v = edge
        tree[u].append(v)
        tree[v].append(u)
    
    visited = [False] * len(a)
    dfs(0, 0, visited, tree, a)
    
    return ans