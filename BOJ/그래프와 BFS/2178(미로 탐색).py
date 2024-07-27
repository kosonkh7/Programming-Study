n, m = map(int, input().split())

arr = []

for i in range(n):
    x = input()
    x_list =[]
    for j in range(m):
        x_list.append(x[j])
    arr.append(x_list)

visited = [[False]*m for _ in range(n)]

min_answer = 10000

def dfs(i, j, answer):
    visited[i][j] = True
    if i == n-1 and j == m-1:
        global min_answer
        min_answer = min(min_answer, answer)
        return
    
    move = False

    if j+1 < m and visited[i][j+1] == False and arr[i][j+1]=='1':
        move = True
        dfs(i, j+1, answer+1)
        visited[i][j+1] = False
    if j-1 >= 0 and visited[i][j-1] == False and arr[i][j-1]=='1':
        move = True
        dfs(i, j-1, answer+1)
        visited[i][j-1] = False
    if i+1 < n and visited[i+1][j] == False and arr[i+1][j]=='1':
        move = True
        dfs(i+1, j, answer+1)
        visited[i+1][j] = False
    if i-1 >= 0 and visited[i-1][j] == False and arr[i-1][j]=='1':
        move = True
        dfs(i-1, j, answer+1)
        visited[i-1][j] = False
    
    if move==False:
        return
    
dfs(0,0,1)

print(min_answer)


"""
위 코드는 올바르게 동작하지만 시간 초과 발생
"""