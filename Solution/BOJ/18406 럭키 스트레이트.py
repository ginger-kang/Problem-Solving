n = input()
left_num = n[:len(n)//2]
right_num = n[len(n)//2:]

left_sum, right_sum = 0, 0
for i in range(len(n)//2):
    left_sum += int(left_num[i])
    right_sum += int(right_num[i])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
