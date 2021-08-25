def dfs(arr):
    global result
    if len(arr) == m:
        print(*arr)
        return

    prev = 0
    for i in range(len(nums)):
        if prev != nums[i]:
            prev = nums[i]
            arr.append(nums[i])
            dfs(arr)
            arr.pop()

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

dfs([])
