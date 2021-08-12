n = int(input())
words = [input() for _ in range(n)]

word_convert = {}
for word in words:
    i = len(word) - 1
    for c in word:
        if word_convert.get(c) is not None:
            word_convert[c] += pow(10, i)
        else:
            word_convert[c] = pow(10, i)
        i -= 1

word_convert = sorted(word_convert.items(), key=lambda x:x[1], reverse=True)

num = 9
ans = 0
for word in word_convert:
    x, y = word
    ans += y * num
    num -= 1

print(ans)
