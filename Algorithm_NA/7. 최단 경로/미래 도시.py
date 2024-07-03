"""
입력값: 회사 개수 N개, 경로 개수 M, 튜플 형태의 M개의 경로, 최종 목적지 X, 중간 목적지 K
중간 목적지를 거쳐 최종 목적지로 향하는 최단 거리를 출력하라. (각 경로 간의 길이는 전부 1, 왕복 가능)
X로 도착이 불가능할 땐 -1을 출력

플로이드 워셜 알고리즘은 시간복잡도가 n^3으로 아주 크지만, 
이 문제는 n, m <= 100으로 범위가 작기 때문에, 구현 방법이 간단한 플로이드 워셜 알고리즘으로 접근하는 것이 유리하다.
"""

n, m = map(int, input().split())
graph = [10000000000 * (n+1) for _ in range(n+1)] # 회사 간 거리 초기화

# 회사 간 연결이 되어 있다면 해당 그래프 값 1로 변경
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신은 거리 0으로 초기화
for i in range(n+1):
    graph[i][i] = 0

# 최종 목적지 x, 중간 목적지 k
x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i]+graph[i][b])

# k를 거쳐 x로 가는 최단 거리
distance = graph[1][k] + graph[k][x]

# x로 갈 수 없으면 -1이 출력되게 구현
if distance >= 10000000000:
    print(-1)
else:
    print(distance)