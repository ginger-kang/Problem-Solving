def check(seq):
    length = len(seq)
    #print(length)
    for i in range(length-1, (length//2)-1, -1):
        l = length - i
        if seq[-l:] == seq[2*(-l):-l]:
            return False
        
    return True

def good_seq(seq):
    if not check(seq):
        return -1
        
    if len(seq) == n:
        print(seq)
        return 0

    for i in range(1, 4):
        seq += str(i)
        if good_seq(seq) == 0:
            return 0
        seq = seq[:-1]
        
n = int(input())
seq = ''
good_seq(seq)
