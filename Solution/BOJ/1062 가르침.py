import sys
input = sys.stdin.readline

def get_max():
    count = 0
    for word in words:
        flag = True
        for c in word:
            if c == '\n':
                break
            if visited[ord(c) - ord("a")] == False:
                flag = False
                break
        if flag:
            count += 1

    return count

def dfs(idx, cnt):
    global result
    
    if cnt == k:
        result = max(result, get_max())
        return
    
    for i in range(idx, 26):
        if visited[i] == False:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False

n, k = map(int, input().split())
words = []
for _ in range(n):
    words.append(input())

visited = [False] * 26

visited[ord("a") - ord("a")] = True
visited[ord("n") - ord("a")] = True 
visited[ord("t") - ord("a")] = True
visited[ord("i") - ord("a")] = True
visited[ord("c") - ord("a")] = True

result = 0

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    for i in range(26):
        if visited[i] == False:
            dfs(i, 5)
    print(result)
