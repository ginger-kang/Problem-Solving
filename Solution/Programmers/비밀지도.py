def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in arr1:
        if len(bin(i)[2:]) < n:
            map1.append('0' * (n-len(bin(i)[2:])) + bin(i)[2:])
        else:
            map1.append(bin(i)[2:])
    for i in arr2:
        if len(bin(i)[2:]) < n:
            map2.append('0' * (n-len(bin(i)[2:])) + bin(i)[2:])
        else:
            map2.append(bin(i)[2:])
    for i in range(n):
        tmp = ''
        for j in range(n):
            if int(map1[i][j]) or int(map2[i][j]):
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer
