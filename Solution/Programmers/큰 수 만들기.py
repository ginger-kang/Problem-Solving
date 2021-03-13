def solution(number, k):
    big = []
    for index, num in enumerate(number):
        while big and big[-1] < num and k > 0:
            big.pop()
            k -= 1
        big.append(num)
    if k > 0:
        while k:
            big.pop()
            k -= 1
    return ''.join(big)
