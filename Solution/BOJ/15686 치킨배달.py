from itertools import combinations

def chicken(mise):
    home = []
    for i in range(n):
        for j in range(n):
            #if maps[i][j] == 2 and (i, j) not in mise:
            #    maps[i][j] = 0
            if maps[i][j] == 1:
                home.append((i,j))
    home_chicken = []
    min_tmp = 0
    for i in home:
        min_tmp = 300
        for j in mise:
            guri = abs(i[0] - j[0]) + abs(i[1] - j[1]) 
            min_tmp = min(guri, min_tmp)
        home_chicken.append(min_tmp)
    return sum(home_chicken)
    

n, m = map(int, input().split(' '))
maps = [list(map(int, input().split(' '))) for _ in range(n)]

tmp = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            tmp.append((i,j))

if len(tmp) == 1:
    print(chicken(tmp))
else:
    ck = []
    ans = 100
    for i in range(1, m+1):
        ck.append(list(combinations(tmp,i)))
    for i in ck:
        for j in i:
            ans = min(chicken(j), ans)
    print(ans)
