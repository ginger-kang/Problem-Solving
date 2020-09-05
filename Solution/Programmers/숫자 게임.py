def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)
    
    result = 0
    for a in A:
        if a >= B[0]:
            continue
        B.pop(0)
        result += 1
    return result
