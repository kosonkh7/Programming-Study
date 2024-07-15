"""
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

BFS로 풀 예정
"""

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0

from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True

for i in range(1, n+1):
    if not visited[i]:
        count+=1
        bfs(i)

print(count)