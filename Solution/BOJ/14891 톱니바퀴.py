def left(num, dd):
    if num == 1:
        return
    if tb[num][6] == tb[num-1][2]:
        return
    else:
        if dd == 1:
            return (num-1, -1)
        elif dd == -1:
            return (num-1, 1)

def right(num, dd):
    if num == 4:
        return
    if tb[num][2] == tb[num+1][6]:
        return
    else:
        if dd == 1:
            return (num+1, -1)
        elif dd == -1:
            return (num+1, 1)

def turn(num, dirc):
    if dirc == 1:
        tb[num] = tb[num][-1] + tb[num][:7]
    else:
        tb[num] = tb[num][1:] + tb[num][0] 

tb = [' ']
for _ in range(4):
    tb.append(input())

k = int(input())
for _ in range(k):
    num, dirc = map(int, input().split(' '))

    result = [(num, dirc)]
    d = dirc
    for i in range(num, 0, -1):
        tmp = left(i, d)
        if not tmp:
            break
        result.append(tmp)
        d = tmp[1]

    d = dirc
    for i in range(num, 4):
        tmp = right(i, d)
        if not tmp:
            break
        result.append(tmp)
        d = tmp[1]

    for num, dirc in result:
        turn(num, dirc)

print(int(tb[1][0])*1 + int(tb[2][0])*2 + int(tb[3][0])*4 + int(tb[4][0])*8)














        
