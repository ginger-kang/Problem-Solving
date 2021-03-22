def solution(distance, rocks, n):
    rocks = sorted(rocks)
    rocks.append(distance)
    left = 0
    right = distance
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        count = 0
        prev = 0
        minVal = int(1e9)
        for rock in rocks:
            if rock - prev < mid:
                count += 1
            else:
                minVal = min(minVal, rock - prev)
                prev = rock
        if count > n:
            right = mid - 1
        else:
            left = mid + 1
            ans = minVal
    return ans
