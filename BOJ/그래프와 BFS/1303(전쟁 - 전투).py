from collections import deque

n, m = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(list(input()))

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

w = 0
b = 0

def bfs(i, j, color):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    count = 1
    
    while queue:
        x, y = queue.popleft()
        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == False and n_list[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    
    return count**2

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            if n_list[i][j] == 'W':
                w += bfs(i, j, 'W')
            else:
                b += bfs(i, j, 'B')

print(w, b)