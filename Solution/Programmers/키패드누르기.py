def middle(key_pad, current_left, current_right, num):
    left = [0,0]
    right = [0,0]
    middle = [0,0]
    for i in range(4):
        for j in range(3):
            if key_pad[i][j] == num:
                middle = [i,j]
            if key_pad[i][j] == current_left:
                left = [i,j]
            if key_pad[i][j] == current_right:
                right = [i,j]
    
    #print(middle, left, right)
    dist_left = abs(middle[0]-left[0]) + abs(middle[1]-left[1])
    dist_right = abs(middle[0]-right[0]) + abs(middle[1]-right[1])
    
    return dist_left, dist_right
                
def solution(numbers, hand):
    key_pad = [[1,2,3], [4,5,6], [7,8,9], [11,0,12]]
    left_number = [1,4,7]
    right_number = [3,6,9]
    answer = ''
    current_left = 11
    current_right = 12
    for i in numbers:
        if i in left_number:
            answer += 'L'
        elif i in right_number:
            answer += 'R'
        else:
            dist_left, dist_right = middle(key_pad, current_left, current_right, i)
            if dist_left > dist_right:
                answer += 'R'
            elif dist_left < dist_right:
                answer += 'L'
            else:
                if hand == 'left':
                    answer += 'L'
                else:
                    answer += 'R'
        if answer[-1] == 'L':
            current_left = i
        else:
            current_right = i
    
    return answer
