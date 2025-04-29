"""
다익스트라 문제에서
1. 최소 거리 비용
2. 최소 거리 경로 출력
"""




"""
최소 거리 경로 출력, 경로 개수


import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]  
distance = [9999999999]*(n+1) # 최단거리 업데이트할 거리 테이블

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

start, end = map(int, input().split())

def djstra(start):
    queue = []
    heapq.heappush(queue, (0, start)) # 최단거리 순으로 빼기 위해 거리를 앞으로
    distance[start] = 0

    while queue:
        d, now = heapq.heappop(queue) # 최단거리가 가장 짧은 노드 꺼내기
        if distance[now] < d: # 현재 노드가 이미 처리된 적 있다면 무시
            if now == end:
                break

        
        for i in graph[now]: # 현재 노드와 인접한 다른 노드 확인
            cost = d + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


djstra(start)

print(distance[end])"""