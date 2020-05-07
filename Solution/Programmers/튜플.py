def solution(s):
    s = s[2:-2].split('},{')
    s_list = []
    s = sorted(s, key = lambda x:len(x))
    answer = []
    tmp = []
    for i in s:
        tmp.append(i.split(','))
    for i in tmp:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer