n = int(input())
cards = list(map(int, input().split()))
cards = sorted(cards)
m = int(input())
data = list(map(int, input().split()))
result = []
for i in data:
    left = 0
    right = n-1
    flag = False
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == i:
            result.append(1)
            flag = True
            break
        elif cards[mid] < i:
            left = mid + 1
        elif cards[mid] > i:
            right = mid - 1
    if not flag:
        result.append(0)

for i in result:
    print(i, end=' ')
