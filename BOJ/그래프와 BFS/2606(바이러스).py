from collections import deque

n = int(input())
t = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(t):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)


def bfs():
    queue = deque([1])
    while queue:
        num = queue.popleft()
        visited[num] = True
        for i in graph[num]:
            if not visited[i]:
                queue.append(i)

bfs()

answer = 0
for i in range(2, n+1):
    if visited[i] == True:
        answer += 1

print(answer)
