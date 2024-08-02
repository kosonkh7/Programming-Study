"""
체스판 위에 한 나이트가 놓여져 있다. 
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.

각 테스트 케이스는 세 줄로 이루어져 있다. 첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

-> 사실 처음에 구현으로 풀고자 했는데, 한 변의 크기를 보고 완탐, BFS로 풀어도 된다는 걸 캐치했어야 했다.
"""
from collections import deque

# 테스트 케이스 수
t = int(input())

# 나이트 이동 가능한 8가지 이동 경로를 방향벡터화
dx = [2, 2, 1, -1, -2, -2, -1, 1]
dy = [-1, 1, 2, 2, 1, -1, -2, -2]

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        nx, ny = queue.popleft() 
        for i in range(8): # 8가지 이동 방향에 대하여
            if 0 <= nx+dx[i] < l and 0 <= ny+dy[i] < l: # 이동한 말 위치가 판 안에 존재 한다면
                if visited[nx+dx[i]][ny+dy[i]] == True: # 이전에 방문했는지 체크
                    continue
                else:
                    arr[nx+dx[i]][ny+dy[i]] = arr[nx][ny] + 1
                    visited[nx+dx[i]][ny+dy[i]] = True
                    queue.append((nx+dx[i], ny+dy[i]))

for _ in range(t):
    l = int(input())
    x, y = map(int, input().split())
    ax, ay = map(int, input().split())

    arr = [[500]*l for _ in range(l)]
    visited = [[False]*l for _ in range(l)]
    arr[x][y] = 0
    visited[x][y] = True

    bfs(x, y)
    print(arr[ax][ay])