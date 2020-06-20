#C#: 1, D#: 2, F#: 3, G#: 4, A#: 5
def replace_sheet(sheet):
    sheet = sheet.replace('C#', '1');
    sheet = sheet.replace('D#', '2');
    sheet = sheet.replace('F#', '3');
    sheet = sheet.replace('G#', '4');
    sheet = sheet.replace('A#', '5');

    return sheet

def solution(m, musicinfos):
    music_box = []
    tmp = '(None)'
    answer = ''
    for music in musicinfos:
        start, end, song, sheet = music.split(',');
        start_hour, start_min = start.split(':');
        end_hour, end_min = end.split(':');
        play_time = (int(end_hour) - int(start_hour)) * 60 + int(end_min) - int(start_min);
        sheet = replace_sheet(sheet);
        sheet = sheet * (play_time // len(sheet)) + sheet[:play_time % len(sheet)]
        music_box.append((song, sheet));
    m = replace_sheet(m);
    print(m, music_box)
    for i in music_box:
        if m in i[1]:
            if tmp != '(None)':
                if len(tmp) < len(i[1]):
                    tmp = i[1];
                    answer = i[0];
            else:
                tmp = i[1];
                answer = i[0];
    if tmp != '(None)':
        return answer
    return '(None)';
