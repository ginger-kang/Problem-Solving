def dfs(root):
    global answer
    
    flag = False
    visited[root] = True
    for i in range(n):
        if node_data[root][i] == 1 and visited[i] == False:
            flag = True
            dfs(i)

    if flag == False:
        answer += 1

n = int(input())
input_data = list(map(int ,input().split(' ')))
node_data = [[0] * n for _ in range(n)]
delete_node = int(input())
root = 0
answer = 0

for i in range(len(input_data)):
    if input_data[i] == -1:
        root = i
    else:
        node_data[i][input_data[i]] = 1
        node_data[input_data[i]][i] = 1


for i in range(n):
    node_data[i][delete_node] = 0
    node_data[delete_node][i] = 0

visited = [False] * n

dfs(root)

print(answer)
