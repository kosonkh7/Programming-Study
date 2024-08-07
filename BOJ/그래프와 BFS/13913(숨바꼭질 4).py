"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""

from collections import deque

n, k = map(int, input().split())

time = [100000] * 100001 # 해당 위치의 최소 시간 담는 리스트
visited = [False] * 100001 # 방문 여부
previous = [100001] * 100001 # 해당 위치로 오기 직전 위치를 담는 리스트

def bfs(n, v):
    queue = deque([(n, v)])
    visited[n] = True
    previous[n] = n
    while queue:
        x, y = queue.popleft()
        time[x] = y
        if x == k: # 목표 위치에 도달하면 반복문 중단
            break

        if x-1 >= 0 and visited[x-1]==False: 
            queue.append((x-1, y+1)) 
            previous[x-1] = x
            visited[x-1] =True

        if x+1 <= 100000 and visited[x+1]==False:
            queue.append((x+1, y+1)) 
            previous[x+1] = x
            visited[x+1] =True

        if 2*x <= 100000 and visited[2*x]==False:
            queue.append((2*x, y+1)) 
            previous[2*x] = x
            visited[2*x] =True                    

bfs(n, 0) # 실행
print(time[k]) # 해당 위치까지 최소 시간


# 해당 위치까지 거쳐가는 경로를 bfs 도중 previous 저장값을 따라가며 조회 
trace = []
start = k

while start != n:
    trace.append(start)
    start = previous[start]

trace.append(n)
trace.reverse()

for i in trace:
    print(i, end=' ')