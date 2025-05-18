# 답은 맞았는데, 시간복잡도 고려 안함. DFS로 푸는 연습도 해보면 좋을 듯
from collections import deque
n, m = map(int, input().split())
n_list = [list(input()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque([[0, 0, 1, list(n_list[0][0])]])
answer = 0

while queue:
    x, y, num, visited = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and n_list[nx][ny] not in visited:
            tmp = visited + list(n_list[nx][ny])
            answer = max(answer, len(tmp))
            queue.append([nx, ny, len(tmp), tmp])

print(answer)