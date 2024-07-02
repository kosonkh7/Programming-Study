# 시간복잡도는 O(ElogV)
# 노드를 하나씩 꺼내 검사하는 반복문(while문)은 노드의 개수 V 이상의 횟수로는 반복되지 않는다.
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 노드 개수, 간선 개수
start = int(input()) # 시작 노드 번호를 입력받기

graph = [[] for i in range(n+1)] # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
distance = [10000000000] *(n+1) # 최단 거리 테이블을 모두 무한으로 초기화

# 모든 간선 정보를 입력 받기
for i in range(m):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미.
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        dist, now = heapq.heappop(q) # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기

        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)


