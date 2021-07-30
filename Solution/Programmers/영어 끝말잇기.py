def solution(n, words):
    turn = 0
    prev_word = []
    person = -1
    for idx, word in enumerate(words):
        if idx % n == 0:
            turn += 1
        if prev_word and word[0] != prev_word[-1][-1] or word in prev_word:
            person = idx
            break
        prev_word.append(word)
    
    if person == -1:
        return [0, 0]
    else:
        return person % n + 1, turn