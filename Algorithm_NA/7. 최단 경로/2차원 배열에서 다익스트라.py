# 한 지점 > 다른 지점 최소 비용 경로 찾는 건 다익스트라
# 모든 지점 > 모든 지점 가는 최소 비용 찾는 건 플로이드 워셜
# 문제: 시작점(0,0)에서 끝점(n-1, n-1)까지 최소 비용으로 갈 때 그 비용은

import heapq

n = int(input())

n_list = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    n_list.append(tmp)

# 방향벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dstra(n, n_list):
    # 시작 위치에서 최소 거리를 저장하기 위한 배열
    distance = [[1000000000]*n for _ in range(n)] # 입력값 2차원 배열과 크기 같음
    distance[0][0] = n_list[0][0] # 시작점 비용
    
    # 우선순위큐
    q = []
    heapq.heappush(q, (n_list[0][0], 0, 0)) # (개수, x좌표, y좌표)
    
    while q:
        now, x, y = heapq.heappop(q)
        
        # 이미 처리된 적 있는 칸은 무시
        if now > distance[x][y]:
            continue
        
        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 이동 범위 내에 있을 때만 조건
            if 0 <= nx < n and 0 <= ny < n:
                after = now + n_list[nx][ny]
                
                # 더 적은 비용으로 헤당 칸에 도착할 수 있는 경우 갱신
                if after < distance[nx][ny]:
                    distance[nx][ny] = after
                    heapq.heappush(q, (after, nx, ny))
    
    return distance[n-1][n-1]
    
    
print(dstra(n, n_list))