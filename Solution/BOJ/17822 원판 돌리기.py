from copy import deepcopy

def turn(wp, idx, d, k):
    if d == 0:
        for _ in range(k):
            t = wp[idx][-1]
            wp[idx] = [t] + wp[idx][:m-1]
    else:
        for _ in range(k):
            wp[idx].append(wp[idx].pop(0))

def check(wp):
    checked = [[False] * m for _ in range(n)]
    for i in range(n):
        tmp = wp[i][0]
        if tmp == wp[i][1] and tmp:
            checked[i][0], checked[i][1] = True, True
        elif tmp == wp[i][m-1] and tmp:
            checked[i][0], checked[i][m-1] = True, True

        tmp = wp[i][m-1]
        if tmp == wp[i][m-2] and tmp:
            checked[i][m-1], checked[i][m-2] = True, True
        elif tmp == wp[i][0] and tmp:
            checked[i][m-1], checked[i][0] = True, True

        for j in range(2, m-1):
            tmp = wp[i][j]
            if tmp == wp[i][j-1] and tmp:
                checked[i][j] = True
                checked[i][j-1] = True
            elif tmp == wp[i][j+1] and tmp:
                checked[i][j] = True
                checked[i][j+1] = True

    for j in range(m):
        if wp[0][j] == wp[1][j] and wp[0][j]:
            checked[0][j] = True
            checked[1][j] = True
        if wp[n-1][j] == wp[n-2][j] and wp[n-1][j]:
            checked[n-1][j] = True
            checked[n-2][j] = True
        for i in range(2, n-1):
            tmp = wp[i][j]
            if tmp == wp[i-1][j] and tmp:
                checked[i][j] = True
                checked[i-1][j] = True
            elif tmp == wp[i+1][j] and tmp:
                checked[i][j] = True
                checked[i+1][j] = True

    flag = 0
    for i in range(n):
        for j in range(m):
            if checked[i][j] == True:
                wp[i][j] = 0
                flag += 1
    cnt = 0
    s = 0
    if flag == 0:
        for i in range(n):
            for j in range(m):
                if wp[i][j] != 0:
                    cnt += 1
                    s += wp[i][j]
        avg = s/cnt
        for i in range(n):
            for j in range(m):
                if wp[i][j] != 0:
                    if wp[i][j] < avg:
                        wp[i][j] += 1
                    elif wp[i][j] > avg:
                        wp[i][j] -= 1

n, m, t = map(int, input().split(' '))
wp = [list(map(int, input().split(' '))) for _ in range(n)]
data = [list(map(int, input().split(' '))) for _ in range(t)]

for i in data:
    x, d, k = i[0], i[1], i[2]
    for j in range(n):
        if (j+1) % x == 0:
            turn(wp, j, d, k)
        else:
            continue
    s = 0
    for i in wp:
        s += sum(i)

    if s == 0:
        break
    else:
        check(wp)
ans = 0
for i in wp:
    ans += sum(i)
print(ans)
