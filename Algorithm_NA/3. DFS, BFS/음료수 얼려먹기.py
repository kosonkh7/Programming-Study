"""
입력값: 가로,세로 길이 n, m / 얼음 틀 모양 (0, 1)
출력값: 얼음 개수

DFS 함수 정의 전략
특정 노드에서 하단과 우측을 조사하여 0이면 재귀적으로 DFS 수행, 1이면 중단. 조사한 노드는 방문 리스트 True로 변경 

모든 노드 순차적으로 조사하면서 (시간복잡도 O(N))
1. 이미 방문 처리된 노드는 건너 뜀
2. 조사 중인 노드가 1이라면, 방문 처리만 함
3. 조사 중인 노드가 0이라면, 얼음 개수 하나를 추가하고 DFS 적용
"""

# 얼음판 크기
n, m = map(int, input().split())

# 얼음판 모양
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 방문 리스트 전부 False로 초기화
visited = [[False]*m for _ in range(n)]

# 제출값
sum = 0

def DFS(graph, x, y, visited):
    # 조사 중인 노드를 방문 처리함
    visited[x][y] = True

    # 조사 중인 노드의 아래 노드가 0인지, 1인지 확인
    while x<n:
        if x+1 >= n:
            break
        # 조사 중인 노드의 아래 노드가 1이라면 방문 처리하고 반복문 종료
        elif graph[x+1][y] == 1:
            visited[x+1][y] = True
            break        
        # 조사 중인 노드의 아래 노드가 0이라면 재귀적으로 다시 DFS 적용
        elif graph[x+1][y] == 0:
            DFS(graph, x+1, y, visited)
            break # 이거 안 걸어서 무한루프 반복되고 난리남!!

    # 조사 중인 노드의 오른쪽 노드가 0인지, 1인지 확인
    while y<m:
        if y+1 >= m:
            break
        elif graph[x][y+1] == 1:
            visited[x][y+1] = True
            break
        elif graph[x][y+1] == 0:
            DFS(graph, x, y+1, visited)
            break # 이거 안 걸어서 무한루프 반복되고 난리남

# 그래프 순차적으로 조사 (시간 복잡도 O(N))
for x in range(n):
    for y in range(m):
        # 1. 이미 방문 처리된 노드는 건너 뜀
        if visited[x][y] == True:
            continue
        # 2. 조사 중인 노드가 1이라면, 방문 처리만 함
        elif graph[x][y] == 1:
            visited[x][y] == True
        # 3. 조사 중인 노드가 0이라면, 얼음 개수 하나를 추가하고 DFS 적용
        elif graph[x][y] == 0:
            sum += 1
            DFS(graph, x, y, visited)

print(sum)


"""
모범 답안

# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
"""