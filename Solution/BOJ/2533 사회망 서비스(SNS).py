import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def dfs(i):
    visited[i] = True
    dp[i][1] = 1
    for e in graph[i]:
        if not visited[e]:
            # 트리 돌면서 dp배열 초기화, leaf 노드까지 내려감
            dfs(e)
            # 현재 노드가 얼리어탑터가 아니면 자식 노드는 무조건 얼리어탑터여야
            # 한다.
            dp[i][0] += dp[e][1]
            # 현재 노드가 얼리어탑터면, 자식 노드는 얼리어탑터이든 아니든 상관
            # 없으므로 둘 중에 작은 값을 더해준다
            dp[i][1] += min(dp[e][0], dp[e][1])

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# dp[i][0] = 내가 얼리어탑터가 아닐 때 필요한 얼리어탑터 수
# dp[i][1] = 내가 얼리어탑터 일 때 필요한 얼리어탑터 수
dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

dfs(1)
print(min(dp[1][0], dp[1][1]))
