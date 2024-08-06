"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
from collections import deque

n, k = map(int, input().split())

map = [100000]*100001
visited = [False]*100001
    
def bfs(n, v):
    visited[n] = True
    map[n] = v
    queue = deque([(n, v)])
    
    while queue:
        x, y = queue.popleft()
        if x-1 >= 0 and visited[x-1]==False:
            queue.append([x-1, y+1])
            visited[x-1] = True
            map[x-1] = y+1
        if x+1 <= 100000 and visited[x+1]==False:
            queue.append([x+1, y+1])
            visited[x+1] = True
            map[x+1] = y+1
        if 2*x <= 100000 and visited[2*x]==False:
            queue.append([2*x, y+1])
            visited[2*x] = True
            map[2*x] = y+1

bfs(n, 0)

print(map[k])


"""
보완할 점 -> 
map은 파이썬 내장함수와 이름이 겹치므로 다른 이름을 사용하는 습관
목표 위치에 도달하면 값을 즉시 반환하도록 코드를 설계하여 불필요한 연산 줄이기
ex) if x == k: return k

"""