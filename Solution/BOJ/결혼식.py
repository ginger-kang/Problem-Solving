def marry(friends, visited):
    global ans
    q = [1]
    cnt = 1
    visited[1] = True
    while q:
        #print(q)
        for _ in range(len(q)):
            x = q.pop(0)
            for i in friends[x]:
                if visited[i] == False and cnt <= 2:
                    ans += 1
                    visited[i] = True
                    q.append(i)
        cnt += 1

n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split(' '))
    friends[a].append(b)
    friends[b].append(a)

ans = 0
visited = [False] * (n+1)
marry(friends, visited)
print(ans)

