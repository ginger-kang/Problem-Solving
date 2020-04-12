N, M = map(int, input().split(' '))

def bt(arr, number, k):
    if k == M:
        for i in arr:
            print(i+1, end = ' ')
        print(end = '\n')
        return

    for i in range(N):
        if number[i] == False:
            arr.append(i)
            number[i] = True
            bt(arr, number, k+1)
            number[i] = False
            arr.pop()
            
number = [False] * N
arr = []

bt(arr, number, 0, 0)
