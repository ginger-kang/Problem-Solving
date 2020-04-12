def shuttle_time(n, t):
    shuttle = []
    shuttle.append("09:00")
    hour = 9
    minute = 0
    for i in range(n-1):
        minute += t
        if minute >= 60:
            hour += 1
            minute = 0
        if hour == 9:
            if minute < 10:
                tmp = "09:0" + str(minute)
                shuttle.append(tmp)
            else:
                tmp = "09:" + str(minute)
                shuttle.append(tmp)
        else:
            if minute < 10:
                tmp = str(hour) + ":0" + str(minute)
            else:
                tmp = str(hour) + ":" + str(minute)
            shuttle.append(tmp)
    return shuttle

def solution(n, t, m, timetable):
    shuttle = shuttle_time(n, t)
    timetable.sort()
    for i in range(n):
        cnt = 0
        if len(timetable) < m:
            return shuttle[-1]
        if i == n-1:
            if timetable[0] > shuttle[i]:
                return shuttle[i]
            hour, minute = timetable[m-1].split(':')
            hour, minute = int(hour), int(minute)
            minute -= 1
            if minute == -1:
                minute = 59
                hour -= 1
            if hour < 10:
                if minute < 10:
                    return "0" + str(hour) + ":0" + str(minute)
                else:
                    return "0" + str(hour) + ":" + str(minute)
            else:
                if minute < 10:
                    return str(hour) + ":0" + str(minute)
                else:
                    return str(hour) + ":" + str(minute)
            
        for j in range(m-1, -1, -1):
                if timetable[j] <= shuttle[i]:
                    timetable.pop(j)
