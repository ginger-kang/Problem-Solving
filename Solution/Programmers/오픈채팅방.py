def solution(record):
    record_data = []
    result = {}
    answer = []
    for i in record:
        record_data.append(i.split(' '))
    #print(record_data)
    for i in record_data:
        if i[0] == 'Leave':
            continue
        else:
            result[i[1]] = i[2]
    for i in record_data:
        if i[0] == 'Enter':
            answer.append(result[i[1]] + "님이 들어왔습니다.")
        if i[0] == 'Leave':
            answer.append(result[i[1]] + "님이 나갔습니다.")
    return answer
