def to_second(time):
    hour, minute, second = time.split(":")

    return int(hour) * 3600 + int(minute) * 60 + int(second)


def second_to_time(sec):
    second = sec % 60
    sec = sec // 60
    minute = sec % 60
    sec = sec // 60
    hour = sec

    return "%02d:%02d:%02d" % (hour, minute, second)


def solution(play_time, adv_time, logs):
    if play_time == adv_time:
        return "00:00:00"

    play_time_sec = to_second(play_time)
    adv_time_sec = to_second(adv_time)

    total_time = [0] * (play_time_sec + 1)
    for log in logs:
        start, end = log.split("-")
        start_sec = to_second(start)
        end_sec = to_second(end)
        total_time[start_sec] += 1
        total_time[end_sec] -= 1

    for i in range(1, play_time_sec):
        total_time[i] += total_time[i - 1]
    for i in range(1, play_time_sec):
        total_time[i] += total_time[i - 1]

    max_val = 0
    max_time = total_time[adv_time_sec]
    for start in range(1, play_time_sec):
        if start + adv_time_sec > play_time_sec:
            end = play_time_sec
        else:
            end = start + adv_time_sec

        sum_time = total_time[end] - total_time[start]
        if max_time < sum_time:
            max_time = sum_time
            max_val = start + 1

    return second_to_time(max_val)
