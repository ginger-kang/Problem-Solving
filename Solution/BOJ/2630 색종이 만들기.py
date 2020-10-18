def same(n, paper, r, c):
    #print(paper)
    flag = paper[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if paper[i][j] != flag:
                return False
    
    return True

def color_paper(n, paper, r, c):
    global ans
    
    if len(paper[r]) == 1:
        return

    if same(n, paper, r, c):
        ans[paper[r][c]] += 1
        return
    
    color_paper(n//2, paper, r + n//2, c)
    color_paper(n//2, paper, r, c + n//2)
    color_paper(n//2, paper, r + n//2, c + n//2)
    color_paper(n//2, paper, r, c)

n = int(input())
ans = [0, 0]
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split(' '))))
color_paper(n, paper, 0, 0)
print(ans[0], end='\n')
print(ans[1])
