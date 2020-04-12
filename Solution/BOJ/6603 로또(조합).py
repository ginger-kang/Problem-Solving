import sys
from itertools import combinations
input = sys.stdin.readline

while 1:
    input_data = list(map(int, input().split(' ')))
    n = input_data[0]
    if n == 0:
        break
    for i in combinations(input_data[1:], 6):
        print(' '.join(map(str, i)))
    print(' ')
