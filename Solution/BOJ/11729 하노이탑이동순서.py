def hanoi(n, f, t, temp):
    if n == 1:
        print(f,t)
    else:
        hanoi(n-1, f, temp , t)
        print(f,t)
        hanoi(n-1, temp, t, f)

n = int(input())

print(2**n-1)
hanoi(n, 1, 3, 2)
