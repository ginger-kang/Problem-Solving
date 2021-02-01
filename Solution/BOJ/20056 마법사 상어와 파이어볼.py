from collections import deque

dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def devide_ball(fire_ball):
    tmp = []
    for pos in fire_ball.keys():
        sum_m = 0
        sum_s = 0
        balls = fire_ball[pos]
        odd = 0
        even = 0
        if len(balls) < 2:
            continue
        for ball in balls:
            m, s, d = ball[0], ball[1], ball[2]
            sum_m += m
            sum_s += s
            if d % 2 != 0:
                odd += 1
            else:
                even += 1

        new_m = sum_m // 5
        if (new_m == 0):
            tmp.append(pos)
        else:
            new_s = sum_s // len(balls)
            fire_ball[pos] = []
            if odd == 0 or even == 0:
                for d in [0, 2, 4, 6]:
                    fire_ball[pos].append([new_m, new_s, d])
            else:
                for d in [1, 3, 5, 7]:
                    fire_ball[pos].append([new_m, new_s, d])
    for i in tmp:
        del fire_ball[i]
    return fire_ball

def move_ball(fire_ball):
    next_fire_ball = {}
    for pos in fire_ball.keys():
        balls = fire_ball[pos]
        r = pos[0]
        c = pos[1]
        for ball in balls:
            m, s, d = ball[0], ball[1], ball[2]
            nr = (r + (dy[d] * s)) % n
            nc = (c + (dx[d] * s)) % n
            if next_fire_ball.get((nr, nc)) is None:
                next_fire_ball[(nr, nc)] = [[m, s, d]]
            else:
                next_fire_ball[(nr, nc)].append([m, s, d])
    return next_fire_ball

n, m, k = map(int, input().split())
fire_ball = {}
for _ in range(m):
    r, c, m, s, d = list(map(int, input().split()))
    fire_ball[(r, c)] = [[m, s, d]]

# fire_ball: r, c, m, s, d
# r -> y, c -> x

for _ in range(k):
    fire_ball = move_ball(fire_ball)
    fire_ball = devide_ball(fire_ball)
#print(fire_ball)

ans = 0
for key in fire_ball.keys():
    for ball in fire_ball[key]:
        ans += ball[0]

print(ans)
