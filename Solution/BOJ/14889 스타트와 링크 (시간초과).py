def sol(arr):
    global minVal
    
    num = []
    for i in range(n):
        num.append(i+1)
    set_num = set(num)
    
    startTeam = arr
    linkTeam = []
    tmp = set_num - set(arr)
    for i in tmp:
        linkTeam.append(i)

    start = 0
    link = 0
    for i in range(n):
        for j in range(n):
            if i+1 in startTeam and j+1 in startTeam:
                start += s[i][j]
            elif i+1 in linkTeam and j+1 in linkTeam:
                link += s[i][j]    

    minVal = min(minVal, abs(start-link))

def team(n, k):
    if k == n//2:
        return sol(arr)
        
    for i in range(n):
        if visited[i] == False:
            arr.append(i+1)
            visited[i] = True
            team(n, k+1)
            arr.pop()
            visited[i] = False

def minVal(x):
    minVal = min(minVal, x)
    return 

n = int(input())
s = [list(map(int, input().split(' '))) for _ in range(n)]
arr = []
visited = [False] * n
minVal = 10000
team(n,0)
print(minVal)
