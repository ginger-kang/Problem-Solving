from sys import stdin
from collections import deque

T = int(input())
for _ in range(T):
    p = stdin.readline().rstrip()
    n = int(input())
    x = deque(stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        x = deque()

    flag =  True
    reverse = False
    for i in p:
        if i == 'R':
            reverse = not reverse
        if i == 'D':
            if not x:
                flag = False
                break
            if reverse:
                x.pop()
            else:
                x.popleft()

    if reverse:
        x.reverse()

    if not flag:
        print('error')
    else:
        print("[",end="")
        for i in range(len(x)):
            print(x[i],end="")
            if i != len(x)-1:
                print(",",end="")
        print("]")
