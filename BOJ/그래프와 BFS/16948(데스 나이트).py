from collections import deque
n = int(input())
visited = [[False]*n for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

answer = -1
queue = deque([(x1, y1, 0)])
visited[x1][y1] = True

while queue:
    x, y, num = queue.popleft()
    
    if x==x2 and y==y2:
        answer = num
        break 

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]==False:
            queue.append((nx, ny, num+1))
            visited[nx][ny] = True
        
print(answer)