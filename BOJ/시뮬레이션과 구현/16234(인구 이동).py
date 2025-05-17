from collections import deque

n, l, r = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]


visited = [[False]*n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
move = True

while move:
    move = False
    visited = [[False]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if visited[i][j] == True:
                continue
            else:
                queue = deque([(i, j)])
                visited[i][j] = True
                tmp = [[i, j]]
                tmp_sum = n_list[i][j]
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(n_list[x][y] - n_list[nx][ny]) <= r:
                            move=True
                            queue.append((nx, ny))
                            tmp.append([nx, ny])
                            tmp_sum += n_list[nx][ny]
                            visited[nx][ny] = True
                
                for a, b in tmp:
                    n_list[a][b] = tmp_sum // len(tmp)

    if move ==True:
        answer += 1 

print(answer)