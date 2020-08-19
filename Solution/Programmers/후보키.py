import itertools

def uniqueness(case, relation):
    unique = []
    for data in relation:
        temp = []
        for c in case:
            temp.append(data[c])
        if temp in unique:
            return False
        else:
            unique.append(temp)
    if len(unique) == len(relation):
        return case

def minimality(case):
    result = [case[0]]
    for i in range(1, len(case)):
        caseSet = set(case[i])
        flag = True
        for j in range(i):
            if caseSet & set(case[j]) == set(case[j]):
                flag = False
        if flag:
            result.append(case[i])
        #print(result)
    return result

def solution(relation):
    row = len(relation[0])
    col = len(relation)
    case = []
    for i in range(1, row+1):
        case += list(itertools.combinations(range(row), i))
        
    result = []
    for c in case:
        if uniqueness(c, relation):
            result.append(uniqueness(c, relation))
    
    #print(result)
    answer = minimality(result)
    return len(answer)
