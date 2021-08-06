import sys
input = sys.stdin.readline

def bisect(target, left, right):
    if left > right:
        return 0
    mid = (left + right) // 2
    if cards[mid] == target:
        return cards[left:right + 1].count(target)
    elif cards[mid] < target:
        return bisect(target, mid + 1, right)
    else:
        return bisect(target, left, mid - 1)

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
sang = list(map(int, input().split()))

cards = sorted(cards)
card_dict = {}
'''
for card in cards:
    if card_dict.get(card) is not None:
        card_dict[card] += 1
    else:
        card_dict[card] = 1
'''
for card in cards:
    left = 0
    right = N - 1
    if not card in card_dict:
        card_dict[card] = bisect(card, left, right)

for i in sang:
    if i in card_dict:
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')
