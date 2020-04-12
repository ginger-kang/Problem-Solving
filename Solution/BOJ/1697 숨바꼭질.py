from collections import deque

n, k = map(int, input().split(' '))

arr = [0] * 100001

def bfs(n):
    q = deque()
    q.append(n)
    while q:
        currentPos = q.popleft()
        if currentPos == k:
            return arr[currentPos]
        for nextPos in (currentPos-1, currentPos+1, currentPos*2):
            if nextPos < 0 or nextPos >= 100001:
                continue
            if arr[nextPos] == 0:
                arr[nextPos] = arr[currentPos] + 1
                q.append(nextPos)

print(bfs(n))
