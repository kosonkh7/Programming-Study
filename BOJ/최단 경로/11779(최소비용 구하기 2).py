import heapq

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)]
distance = [9999999999] * (n+1)
path = [[i] for i in range(n+1)]

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

start, end = map(int, input().split())


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        d, now = heapq.heappop(queue)

        if distance[now] < d: # 이미 조회한 적 있고, 그게 더 비용이 작으면 넘기기
            continue

        for i in graph[now]:
            cost = d + i[1] # 현재에서 다음 노드까지 가는 비용
            if cost < distance[i[0]]: # 만약에 최소 비용 갱신 필요하면
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
                path[i[0]] = path[now] + [i[0]] # 현재까지 최소 경로에 다음 경로 이어 붙임

dijkstra(start)

print(distance[end])
print(len(path[end]))

for i in path[end]:
    print(i, end=' ')