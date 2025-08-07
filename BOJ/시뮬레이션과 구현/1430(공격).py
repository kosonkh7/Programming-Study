"""
구해야할 것
1. 각 탑과 적 사이 거리
2. 각 탑과 탑 사이 거리

탑과 탑 사이의 연결 그래프 구하기. -> 적 위치를 정점으로 한 트리 만들기

그리고 각 탑이 적까지 닿기 위한 횟수(조금 어색한 표현)를 2의 제곱수로 해서 에너지 나눠주기. 
"""
from collections import deque
n, r, d, x, y = map(int, input().split()) # 탑 개수, 사정거리, 초기 에너지, 적 위치 x y
n_list = [list(map(int, input().split())) for _ in range(n)] # 탑 위치 리스트

# 탑과 적 사이의 거리 t_e
t_e = [0] * (n)
for i in range(n):
    xt, yt = n_list[i]
    tmp = ((x-xt)**2 + (y-yt)**2)**(0.5)
    t_e[i] = tmp

# 탑과 적 사이 닿는지 is_t
is_t = [False] * n
for i in range(n):
    if t_e[i] - r <= 0:
        is_t[i] = True

# 탑과 탑 사이의 거리 t_t
t_t = [[0]*n for _ in range(n)]
for i in range(n):
    x1, y1 = n_list[i]
    for j in range(n):
        if t_t[i][j] != 0: continue
        else:
            x2, y2 = n_list[j]
            tmp = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
            t_t[i][j] = tmp
            t_t[j][i] = tmp

# print(t_t)        

# 방문 테이블 (각 탑이 적에 닿는 데 몇 번 거쳐야 하는지. 방문 안했으면 -1)
visited = [-1] * n 

# BFS로 적과 탑까지 몇 번이나 거쳐야 하는지
queue = deque([])
for i in range(n):
    if is_t[i]: # 각 탑이 적과 다이렉트로 연결 되면 0번
        queue.append([i, 0])
        visited[i] = 0

while queue:
    a, num = queue.popleft()
    for i in range(n):
        if visited[i] == -1 and t_t[a][i] <= r:
            visited[i] = num+1
            queue.append([i, num+1])

answer = 0
for i in range(n):
    if visited[i] >= 0:
        answer += d / ((2)**visited[i]) # 각 탑이 적까지 닿기 위해 거치는 횟수를 2의 제곱수로 해서 분모로.

# print(visited)
print(answer)