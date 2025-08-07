"""
4
1 2
1 3
2 4
1 2 4 3
"""
from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
compare = deque(map(int, input().split()))

visited = [False]*(n+1)


index = 0
def dfs(compare):
    x = compare.popleft()
    if not compare:
        print(1)
        exit()
    visited[x]= True
    for _ in range(len(graph[x])):
        if compare[0] in graph[x] and not visited[compare[0]]:
            dfs(compare)
    
if compare[0] != 1:
    print(0)
else:
    dfs(compare)
    print(0)



