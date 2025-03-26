from collections import deque

answer = -1

n = int(input())
x, y = map(int, input().split())
m = int(input())
visited = [False] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    father, son = map(int, input().split())
    graph[father].append(son)
    graph[son].append(father)

queue = deque([[x, 0]])
visited[x] = True

while queue:
    a, num = queue.popleft()
    if a == y:
        answer = num
        break
    else:    
        for i in graph[a]:
            if visited[i]==False:
                visited[i]=True
                queue.append([i, num+1])

print(answer)
            