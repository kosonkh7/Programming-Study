n = int(input())

graph = []

for i in range(n):
    x, y = map(int, input().split())
    graph.append((x,y))

arrive, health = map(int, input().split())

graph.append((arrive, 0))

answer = 10000000000

visited = 0

def dfs(graph, v, visited, health):
    if v == n:
        answer = min(answer, visited)
        return
    for i in range(v+1, n+1):
        after, food = graph[i]
        if after-graph[v][0] > health:
            continue
        else:
            dfs(graph, v, visited+1, health - (after-graph[v][0]) + food)
    

dfs(graph, 0, visited, health)

print(answer)