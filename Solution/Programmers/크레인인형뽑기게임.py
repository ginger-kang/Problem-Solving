def game(line, board, basket):
    cnt = 0
    for i in range(len(board)):
        if board[i][line] == 0:
            continue
        else:
            if len(basket) == 0:
                basket.append(board[i][line])
            else:
                if basket[-1] == board[i][line]:
                    basket.pop(-1)
                    cnt += 2
                else:
                    basket.append(board[i][line])
            board[i][line] = 0
            return cnt
    return cnt
        
def solution(board, moves):
    n = len(board)
    basket = []
    answer = 0
    for i in moves:
        answer += game(i-1, board, basket)
        
    return answer