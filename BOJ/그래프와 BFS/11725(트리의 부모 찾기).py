from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():
    queue = deque([1])
    while queue:
        x = queue.popleft()
        visited[x] = True
        for i in graph[x]:
            if not visited[i]:
                parent[i] = x
                queue.append(i)

bfs()

for i in range(2, n+1):
    print(parent[i])