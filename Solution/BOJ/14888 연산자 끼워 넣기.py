def dfs(i, current_value):
    global arr, op, result
    
    if i == n-1:
        result.append(current_value)
        return
    else:
        if op[0] > 0:
            op[0] -= 1
            dfs(i+1, current_value + arr[i+1])
            op[0] += 1
        if op[1] > 0:
            op[1] -= 1
            dfs(i+1, current_value - arr[i+1])
            op[1] += 1
        if op[2] > 0:
            op[2] -= 1
            dfs(i+1, current_value * arr[i+1])
            op[2] += 1
        if op[3] > 0:
            op[3] -= 1
            if current_value < 0:
                dfs(i+1, -1 * (abs(current_value) // arr[i+1]))
            else:
                dfs(i+1, current_value // arr[i+1])
            op[3] += 1

n = int(input())
arr = list(map(int, input().split(' ')))
op = list(map(int, input().split(' ')))
result = []
dfs(0, arr[0])

print(max(result), end='\n')
print(min(result))
