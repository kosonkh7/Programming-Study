# 각 노드 별 연결(인접) 정보를 2차원 리스트로 표현 -> 여기서 편의상 1~8번 노드로 표현하기 위해 0번 노드 비워둠
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 방문 정보 리스트, 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9


def DFS(graph, v, visited):
    """
    graph: 각 노드 별 연결 정보 2차원 리스트
    v: 노드의 인덱스
    visited: 방문 정보 리스트
    """
    # 현재 노드 v를 방문처리
    visited[v] = True
    # 방문 했다는 걸 보여주기 위한 출력문
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드들을 재귀적으로 방문하게 설계
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

# DFS(graph, 1, visited)

from collections import deque

# 내가 설계한 함수. 예시와 거의 비슷
def BFS(graph, start, visited):
    queue = deque([start])
    visited[start]=True

    while len(queue) > 0:
        for i in graph[queue[0]]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
        print(queue[0], end=' ')
        queue.popleft()

BFS(graph, 1, visited)

# 교재 예시 함수
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True







