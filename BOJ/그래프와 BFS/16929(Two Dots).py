# 처음에 BFS로 했는데 사이클 규칙 찾기가 애매해서, 사이클을 한 번에 찾기 위해서 백트래킹(DFS)를 하는 방법으로 구현했다.

n, m = map(int, input().split())
n_list = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, x1, y1, move):
    global answer
    if answer == 'Yes':
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < n and 0 <= ny < m and move >= 3 and nx == x1 and ny == y1:
            answer = 'Yes'
            return
        elif 0 <= nx < n and 0 <= ny < m and n_list[nx][ny] == n_list[x1][y1] and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, x1, y1, move+1)
            visited[nx][ny] = False   

answer = 'No'
for i in range(n):
    for j in range(m):
        if answer == 'Yes':
            break
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j, i, j, 0)
            
print(answer)