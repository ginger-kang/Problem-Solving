def solve(depth, idx, l, c):
    if depth == l:
        passwords.append(''.join(map(str, pw)))
        return
    for i in range(idx, c):
        pw.append(string[i])
        solve(depth+1, i+1, l, c)
        pw.pop()

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return
        
l, c = map(int, input().split(' '))
string = list(map(str, input().split()))
string.sort()
pw = []
passwords = []

#print(string)
solve(0, 0, l, c)
password(passwords)
