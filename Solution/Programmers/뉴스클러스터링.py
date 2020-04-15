from collections import Counter

def solution(str1, str2):
    set1 = []
    set2 = []
    for i in range(1, len(str1)):
        if str1[i-1:i+1].isalpha():
            set1.append(str1[i-1:i+1].lower())
    for i in range(1, len(str2)):
        if str2[i-1:i+1].isalpha():
            set2.append(str2[i-1:i+1].lower())
    
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    intersection = counter1 & counter2
    union = counter1 | counter2
    
    if not intersection:
        if not union:
            return 65536
        else:
            return 0
    
    i, u = 0, 0
    for e, v in intersection.items():
        i += v
    for e, v in union.items():
        u += v
    
    return int((i/u)*65536)