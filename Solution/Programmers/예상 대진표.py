def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a
        
    while True:
        if b - a > 1 or b % 2 != 0:
            if a % 2 == 0:
                a /= 2
            else:
                a = (a+1) // 2
            if b % 2 == 0:
                b /= 2
            else:
                b = (b+1) // 2
            answer += 1
        else:
            break
    return answer