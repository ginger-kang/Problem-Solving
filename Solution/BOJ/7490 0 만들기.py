def dfs(nums, i):
    global result
    
    if i == n:
        if eval(nums.replace(" ", "")) == 0:
            result.append(nums)
        return

    dfs(nums + "+" + str(i+1), i+1)
    dfs(nums + "-" + str(i+1), i+1)
    dfs(nums + " " + str(i+1), i+1)

T = int(input())
for t in range(T):
    n = int(input())
    result = []
    dfs("1", 1)
    result.sort()
    for i in result:
        print(i)
    if t != T - 1:
        print()
