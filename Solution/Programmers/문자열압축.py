def compress(string):
    result = ''
    count = 1
    for i in range(1, len(string)):
        if string[i] == string[i-1]:
            count += 1
        else:
            if count == 1:
                result += string[i-1]
            else:
                result += str(count)
                result += string[i-1]
            count = 1
    if string[-1] == string[-2]:
        result += str(count)
        result += string[-1]
    else:
        result += string[-1]

    return len(result)

def solution(s):
    length = len(s)//2
    answer = 10000
    for i in range(1, length+1):
        tmp = []
        ss = s
        while ss:
            tmp.append(ss[:i])
            ss = ss[i:]
        answer = min(answer, compress(tmp))
        
    return answer