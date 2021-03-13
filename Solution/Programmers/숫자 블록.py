import math

def solution(begin, end):
    ans = []
    for i in range(begin, end + 1):
        isPrime = True
        if i == 1:
            ans.append(0)
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i // j > 10000000:
                continue
            if i % j == 0:
                ans.append(i // j)
                isPrime = False
                break
        if isPrime:
            ans.append(1)
    return ans
