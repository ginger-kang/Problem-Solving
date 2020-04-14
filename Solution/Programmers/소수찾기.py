import itertools

def ss(num):
    if num == 1:
        return False
    if num % 2 == 0:
        return (num==2)
    for i in range(3, num, 2):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    tmp = []
    for i in numbers:
        tmp.append(i)
    
    sosu = []
    for i in tmp:
        if ss(int(i)) and not int(i) in sosu:
            sosu.append(int(i))
            
    for i in range(1, len(tmp)):
        arr = list(itertools.permutations(tmp, i+1))
        pm = [''] * len(arr)
        for j in range(len(arr)):
            for k in range(i+1):
                pm[j] += arr[j][k]
        for e in pm:
            if ss(int(e)) and not int(e) in sosu:
                sosu.append(int(e))
                
    return len(sosu)