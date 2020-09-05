import sys
sys.setrecursionlimit(10**6)

def hotel(node, room):
    # 해당 방이 배정되지 않았을 경우 바로 방 배정
    # 방 배정 후 node에 room+1 저장
    if not room in node:
        node[room] = room + 1
        return room
    empty = hotel(node, node[room])
    node[room] = node[empty]
    return empty
        
def solution(k, room_number):
    result = []
    node = {}
    for room in room_number:
        temp = hotel(node, room)
        result.append(temp)
    return result
