"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
"""

from collections import deque
# 테스트케이스 횟수 
k = int(input())

def bfs(v):
    queue = deque([v])
    visited[v] = True # 방문처리
    color[v] = 1 # 색깔 우선 1로 지정
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                color[i] = abs(1-color[v]) # 기준과 반대 색 지정
                queue.append(i)
            elif color[i] == color[v]: # 인접했고 이미 방문했는데, 색이 같으면 NO 반환
                return 'NO'
    return 'YES'



for _ in range(k):
    n, m = map(int, input().split())
    graph = [[] for x in range(n+1)]
    visited = [False] * (n+1)
    color = [-1] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a) 
        
    for i in range(1, len(visited)):
        if not visited[i]: # 방문하지 않은 노드 대상으로 bfs 실행
            answer = bfs(i)
            if answer =='NO': 
                break
        else:
            continue
    print(answer)
