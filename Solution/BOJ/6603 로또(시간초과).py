def sol(visit, count):
    if count == 6:
        if set(arr) not in lottoSet:
            for i in arr:
                print(i, end = ' ')
            print()
        lottoSet.append(set(arr))
        return

    for i in range(len(s)):
        if visit[i] == False:
            arr.append(s[i])
            visit[i] = True
            sol(visit, count+1)
            visit[i] = False
            arr.pop()

while True:
    input_data = list(map(int, input().split(' ')))
    if input_data[0] == 0:
        break

    k = input_data[0]
    s = input_data[1:]
    visit = [False]*len(s)
    arr = []
    lottoSet = []

    sol(visit, 0)
    
        
    
