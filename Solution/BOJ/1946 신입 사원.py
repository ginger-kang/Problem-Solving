t = int(input())
for _ in range(t):
    n = int(input())
    grade = []
    for _ in range(n):
        data = list(map(int, input().split(' ')))
        grade.append(data)

    grade = sorted(grade, key = lambda x: x[0])

    min_grade = grade[0][1]
    ans = 0
    for i in range(1, n):
        if grade[i][1] > min_grade:
            ans += 1
        else:
            min_grade = grade[i][1]

    print(n-ans)
        
    
        
