import math

n = int(input())

arr = [True for _ in range(4000001)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

prime = []
for i in range(2, n+1):
    if arr[i]:
        prime.append(i)
#print(prime)
prefix_sum = [0]
sum_val = 0
for i in prime:
    sum_val += i
    prefix_sum.append(sum_val)
#print(prefix_sum)
start = 0
end = 1
ans = 0
while end < len(prefix_sum):
    diff = prefix_sum[end] - prefix_sum[start]
    if diff < n:
        end += 1
    elif diff > n:
        start += 1
    elif diff == n:
        ans += 1
        start += 1
    #print('start = ', start, 'end = ', end, 'diff = ', diff, 'ans = ', ans)
print(ans)
