"""
BOJ에서 정답이 여러가지인 경우에는 스페셜 저지를 사용한다. 
스페셜 저지는 유저가 출력한 답을 검증하는 코드를 통해서 정답 유무를 결정하는 방식이다. 
오늘은 스페셜 저지 코드를 하나 만들어보려고 한다.

정점의 개수가 N이고, 정점에 1부터 N까지 번호가 매겨져있는 양방향 그래프가 있을 때, BFS 알고리즘은 다음과 같은 형태로 이루어져 있다.

큐에 시작 정점을 넣는다. 이 문제에서 시작 정점은 1이다. 1을 방문했다고 처리한다.
큐가 비어 있지 않은 동안 다음을 반복한다.
큐에 들어있는 첫 정점을 큐에서 꺼낸다. 이 정점을 x라고 하자.
x와 연결되어 있으면, 아직 방문하지 않은 정점 y를 모두 큐에 넣는다. 모든 y를 방문했다고 처리한다.
2-2 단계에서 방문하지 않은 정점을 방문하는 순서는 중요하지 않다. 따라서, BFS의 결과는 여러가지가 나올 수 있다.

트리가 주어졌을 때, 올바른 BFS 방문 순서인지 구해보자.

첫째 줄에 정점의 수 N(2 ≤ N ≤ 100,000)이 주어진다. 
둘째 줄부터 N-1개의 줄에는 트리의 간선 정보가 주어진다.
 마지막 줄에는 BFS 방문 순서가 주어진다. 
 BFS 방문 순서는 항상 N개의 정수로 이루어져 있으며, 1부터 N까지 자연수가 한 번씩 등장한다.

입력으로 주어진 BFS 방문 순서가 올바른 순서면 1, 아니면 0을 출력한다.

4
1 2
1 3
2 4
1 3 4 2

올바른 순서는 1, 2, 3, 4와  1, 3, 2, 4가 있다.
"""

from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
compare = list(map(int, input().split()))

visited = [False] * (n+1)
visited[1] = True
queue = deque([[1, 1]]) # [시작 노드, 몇 층인지]

y_list = [0] * (n+1)
y_list[1] = 1

answer = 1
is_visited_all = 0
while queue:
    x, y = queue.popleft()
    is_visited_all += 1

    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            y_list[i] = y+1
            queue.append([i, y+1])

c_index = 1
for c in compare:
    if y_list[c] < c_index:
        answer = 0
        break
    elif y_list[c] > c_index:
        c_index = y_list[c]

if is_visited_all != n:
    answer = 0

print(answer)


"""
1(1) 2(2) 3(2) 4(3)  <- 이 접근 자체가 틀림.

왜냐하면 단순히 높이만 비교하고 있고, 큐에 들어간 순서를 전혀 고려하고 있지 않기 때문(내가 bfs를 대충 이해한 탓)

반례
6
1 2
1 3
2 4
3 5
3 6
1 3 2 5 6 4 <- 틀렸는데 내 코드에선 맞게 출력


모범 코드 (인덱스를 활용해서 비교)
from collections import deque

# 노드 수 입력 받기
n = int(input())

# 트리 구조 저장을 위한 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]

# 트리의 간선 정보 입력 받기 (양방향 연결)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 주어진 BFS 방문 순서 입력 받기
order = list(map(int, input().split()))

# BFS 탐색은 반드시 1번 노드부터 시작해야 함
if order[0] != 1:
    print(0)  # 잘못된 시작 노드일 경우
    exit()

# 방문 여부를 기록하는 리스트
visited = [False] * (n + 1)
visited[1] = True  # 1번 노드는 시작점으로 미리 방문 처리

# BFS 큐 초기화
queue = deque([1])

# order 리스트에서 현재 확인 중인 인덱스 (다음 방문할 노드 위치)
idx = 1  # order[0]은 이미 1번으로 확인했으므로 idx는 1부터 시작

# BFS 탐색 시작
while queue:
    current = queue.popleft()  # 현재 노드

    # current 노드의 아직 방문하지 않은 자식 노드들을 수집
    children = []
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            children.append(neighbor)

    # 현재 노드의 자식 수만큼 다음 방문 순서를 확인해야 함
    child_count = len(children)

    # order 리스트에서 현재 위치부터 다음 자식 수만큼 추출
    expected_children = order[idx:idx + child_count]

    # 현재 자식 노드들과, 주어진 순서에서의 자식 노드가 다르면 틀린 순서
    if set(children) != set(expected_children):
        print(0)
        exit()

    # 자식 노드 순서를 그대로 큐에 넣음 (order 순서를 따름)
    queue.extend(expected_children)

    # order 인덱스를 자식 수만큼 이동
    idx += child_count

# 모든 검사를 통과하면 올바른 BFS 순서임
print(1)

"""