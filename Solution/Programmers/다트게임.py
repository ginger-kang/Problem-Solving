def solution(dartResult):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = ['#', '*']
    dart = []
    tmp = ''
    for idx, i in enumerate(dartResult):
        if i in bonus:
            dart[-1] = int(dart[-1])**bonus[i]
            continue
        elif i in option:
            option_index = (idx // 3)
            if i == '*':
                dart[option_index] *= 2
                if 0 <= option_index - 1 < 3:
                    dart[option_index-1] *= 2
            else:
                dart[option_index] *= -1
            continue
        else:
            if i == '0':
                if dart:
                    if dart[-1] != '1':
                        dart.append(i)
                    else:
                        dart[-1] = '10'
                else:
                    dart.append(i)
            else:
                dart.append(i)
            
    return sum(dart)
    
solution('1D2S3T*')