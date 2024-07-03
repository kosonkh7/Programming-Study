"""
입력값: 도시의 개수 N, 통로의 개수 M. 메시지를 보내고자히는 도시 C | 도시 X에서 도시 Y로 전달, Z 시간 소요 (M개)
출력값: 메세지를 받을 수 있는 도시의 총 개수와, 이때 최단시간

도시 C를 기준으로 다른 도시로 갈 때 최단 거리를 구하는 다익스트라 알고리즘으로 접근하면 좋다.
다익스트라 구현은 익숙해져야 하므로, 다시 풀어보길 권함.
"""
import heapq 

n, m, c = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [10000000000] * (n+1)

# 도시 X에서 도시 Y로 전달된 때 Z시간 초기화
for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우 업데이트 + 큐 삽입
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != 10000000000:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)