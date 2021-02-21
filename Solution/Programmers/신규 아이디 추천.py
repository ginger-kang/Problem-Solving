import re

op = ['-', '_', '.']

def solution(new_id):
    new_id = new_id.lower()
    tmp = ''
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in op:
            tmp += c
    new_id = tmp
    new_id = re.sub('\.\.*', '.', new_id)
    new_id = re.sub('^\.|\.$', '', new_id)
    if not new_id:
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = re.sub('\.$', '', new_id)
    if len(new_id) <= 2:
        last = new_id[-1]
        while len(new_id) != 3:
            new_id += last
    return new_id
