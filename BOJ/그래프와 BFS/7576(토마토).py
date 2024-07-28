from copy import deepcopy

m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = deepcopy(arr)
visited = [[False]*m for _ in range(n)]

from collections import deque

tomato1 = [] # 처음부터 익은 토마토가 존재하는 위치를 큐에 넣기 위한 리스트
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            tomato1.append((0, i, j))
            visited[i][j] = True # 이미 익은 토마토 있는 곳은 방문 처리

        elif arr[i][j] == -1:
            visited[i][j] = True # 토마토 없는 칸도 방문 처리

# 방향 벡터 설정
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque(tomato1) # 이미 익은 토마토 큐에 넣고

    while queue:
        v, x, y = queue.popleft()
        visited[x][y] = True
        for k in range(4): # 인접한 칸 조사
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= n or nx < 0 or ny >= m or ny < 0: # 범위 초과하면 무시
                continue
            if visited[nx][ny] == True: # 이미 방문했거나, 토마토가 없으면 무시
                continue
            else: # 날짜 더해서 큐에 넣어줌
                queue.append((v+1, nx, ny))
                visited[nx][ny] = True
                arr[nx][ny] = v+1 
                # print(nx, ny) 제대로 동작하나 확인하고 싶을 때

bfs()

allone = True
iszero = False
answer = -1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            iszero = True
        if arr2[i][j] != 1: 
            allone = False
        answer = max(answer, arr[i][j])

if allone == True: # 처음부터 전부 익어있었으면 0
    print(0)
elif arr == arr2: # bfs 한 번도 실행 안 됐으면 0
    print(0)
elif iszero == True: # 익지 않은 토마토 존재하면 -1
    print(-1)
else: # 최대값 반환
    print(answer)

