"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 
이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. 
u와 v는 서로 다르며 w는 10 이하의 자연수이다. 
서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

입력
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

출력
0
2
3
7
INF
"""

import heapq

v, e = map(int, input().split()) # 정점, 간선 개수
k = int(input()) # 시작 정점
graph = [[] for _ in range(v+1)]
INF = int(1e9)

for _ in range(e):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

dp = [INF] * (v+1)
dp[k] = 0

def dijkstra(start):
    q= []
    heapq.heappush(q,(0,start))
    dp[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dp[now] < dist:
            continue

        #현재 노드와 연결된 인접 노드 확인
        for i in graph[now]:
            cost =dist+ i[1]
            if cost < dp[i[0]] :
                dp[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(k)

for i in range(1,v+1):
    if dp[i] == INF:
        print("INF")
    else: print(dp[i])