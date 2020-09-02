n, s = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))

prefix = [0]
temp = 0
for i in range(n):
    temp += arr[i]
    prefix.append(temp)

left = 0
right = 1
result = 1000001

while left != n:
    if prefix[right] - prefix[left] < s:
        if right != n:
            right += 1
        else:
            left += 1
    else:
        if right - left < result:
            result = right-left
        left += 1

if result == 1000001:
    print(0)
else:
    print(result)
