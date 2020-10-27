import sys

input = sys.stdin.readline

n, k = map(int, input().split(' '))
belt = list(map(int, input().split(' ')))
robot = []

count = 1
while True:
    #print(robot)
    # rotate belt
    belt = belt[-1:] + belt[:-1]
    for i in range(len(robot)):
        robot[i] += 1
    if (n-1) in robot:
        robot.remove(n-1)

    # rotate robot
    flag = False
    if robot:
        if robot[0] == n-2 and belt[n-1] >= 1:
            robot.pop(0)
            belt[n-1] -= 1
            flag = True
        else:
            next_robot = robot[0] + 1
            if not next_robot in robot and belt[next_robot] >= 1:
                robot[0] = next_robot
                belt[next_robot] -= 1

    if flag:
        idx = 0
    else:
        idx = 1
    for i in range(idx, len(robot)):
        next_robot = robot[i] + 1
        if not next_robot in robot and belt[next_robot] >= 1:
            robot[i] = next_robot
            belt[next_robot] -= 1
    
    # robot
    if 0 not in robot and belt[0] != 0:
        robot.append(0)
        belt[0] -= 1

    if belt.count(0) >= k:
        print(count)
        break
    else:
        count += 1
    
