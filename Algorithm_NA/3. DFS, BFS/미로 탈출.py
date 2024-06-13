"""
입력값: 미로 크기 n, m / 미로 모양 (2차원 배열)
출력값: 미로 탈출을 위한 최소 이동 개수

전략:
1. 미로 공간 범위 밖의 인덱스 제거 설정
2. 조사 중인 노드를 방문 처리 후, 상하좌우 큐에 넣음 
3. 
"""

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 방향 벡터 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append(x, y)
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 조사 중인 노드에서 4방향으로 조사
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽을 만난 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 조사하지 않은 노드라면(1일 때 조사 안함. 2이상은 조사했다는 것을 의미), 현재 노드의 값에 1을 더하여 저장
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 출구(가장 오른쪽 아래) 좌표 반환
    return graph[n-1][m-1]
    
print(BFS(0,0))