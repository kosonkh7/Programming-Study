import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
distance = [10000000000000]*(n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())

def dstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        d, now = heapq.heappop(queue) # 가장 최단거리가 짧은 노드 꺼내기
        if distance[now] < d: # 현재 노드가 이미 처리된 적 있다면 무시
            if now == end:
                break
            else:
                continue
        for i in graph[now]: # 현재 노드와 연결된 다른 인접 노드 확인
            cost = d + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


dstra(start)

print(distance[end])