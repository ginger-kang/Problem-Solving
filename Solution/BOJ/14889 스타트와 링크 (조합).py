from itertools import combinations

n = int(input())
maps = [list(map(int, input().split(' '))) for _ in range(n)]
num = [i for i in range(n)]

sl = list(combinations(num, n//2))

minVal = 10000
for teamA in sl:
    teamB = list(set(num) - set(teamA))

    a = list(combinations(teamA, 2))
    b = list(combinations(teamB, 2))

    scoreA = 0
    scoreB = 0
    for x, y in a:
        scoreA += maps[x][y] + maps[y][x]

    for x, y in b:
        scoreB += maps[x][y] + maps[y][x]

    minVal = min(minVal, abs(scoreA - scoreB))

print(minVal)
