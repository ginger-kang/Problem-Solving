n = int(input())
tower = list(map(int, input().split()))
stack = []
for i, tower in enumerate(tower):
    while True:
        if not stack:
            print(0, end=' ')
            stack.append((tower, i))
            break
        else:
            if stack[-1][0] < tower:
                stack.pop()
            else:
                print(stack[-1][1]+1, end=' ')
                stack.append((tower, i))
                break
