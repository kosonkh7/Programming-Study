"""
검색으로 중요한 힌트를 얻었다.
방문 테이블을 3차원으로 구성해야 되나 싶었는데, 
돌의 총량은 고정이기 때문에 최소값, 최대값으로 방문 테이블을 구성하고, 중간 값은 전체 개수에서 뺌으로써 구할 수 있다더라

문제를 읽고 논리적인 부분을 잘 파악하자.

방문 테이블 설계만 알고 나니까 BFS를 통해 차분히 풀이가 가능했다.
"""
from collections import deque
x = list(map(int, input().split()))
x.sort()

visited = [[False] * (sum(x) + 1) for _ in range((sum(x) + 1))]

queue = deque([x])
visited[x[0]][x[2]] = True
answer = 0

while queue:
    a, b, c = queue.popleft()
    if a==b and b==c and c==a:
        answer = 1
        break
    
    if a != b and a != 0:
        p = a*2
        q = b-a
        tmp = sorted([p, q, c])
        if not visited[tmp[0]][tmp[2]]:
            visited[tmp[0]][tmp[2]] = True
            queue.append(tmp)
    
    if a != c and a != 0:
        p = a*2
        q = c-a
        tmp = sorted([p, q, b])
        if not visited[tmp[0]][tmp[2]]:
            visited[tmp[0]][tmp[2]] = True
            queue.append(tmp)
    
    if b != c and b != 0:
        p = b*2
        q = c-b
        tmp = sorted([p, q, a])
        if not visited[tmp[0]][tmp[2]]:
            visited[tmp[0]][tmp[2]] = True
            queue.append(tmp)

print(answer)