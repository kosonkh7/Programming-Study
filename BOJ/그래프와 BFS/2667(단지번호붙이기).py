"""

"""

n = int(input())
board = [input() for _ in range(n)]
visited = [[False]*n for _ in range(n)]
count=0
n_list = []

def dfs(i, j):
    global num
    visited[i][j] = True
    num += 1
    if i+1 < n and visited[i+1][j] == False and board[i+1][j] == '1':
        dfs(i+1, j)
    if j+1 < n and visited[i][j+1] == False and board[i][j+1] == '1':
        dfs(i, j+1)    
    if i > 0 and visited[i-1][j] == False and board[i-1][j] == '1':
        dfs(i-1, j)
    if j > 0 and visited[i][j-1] == False and board[i][j-1] == '1':
        dfs(i, j-1)
    return num
    

for i in range(n):
    for j in range(n):
        if board[i][j]=='0' or visited[i][j]==True:
            visited[i][j] = True
            continue
        else:
            count += 1
            num = 0
            dfs(i, j)
            n_list.append(num)

print(count)

for i in sorted(n_list):
    print(i)
