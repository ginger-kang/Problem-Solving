import sys
input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))

left = 0
right = n - 1

result = [abs(arr[left] + arr[right]), [left, right]]
while left < right:
    val = arr[left] + arr[right]
    if result[0] > abs(val):
        result[0] = abs(val)
        result[1] = [left, right]
        if val == 0:
            break
    if val > 0:
        right -= 1
    else:
        left += 1
        
print(arr[result[1][0]], end=' ')
print(arr[result[1][1]])
