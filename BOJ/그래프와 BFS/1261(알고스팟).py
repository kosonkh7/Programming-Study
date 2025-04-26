"""
처음에서 마지막 셀까지 방문할 수 있는 최소 벽 부수는 개수를 구하는 것.

각 위치까지 최소로 부수고 도달할 수 있는 개수를 담은 테이블을 만들어서 해결.
"""
from collections import deque

m, n = map(int, input().split())
n_list = []
for i in range(n):
    tmp = input()
    tmp_list = [int(j) for j in tmp]
    n_list.append(tmp_list)


nx = [1, -1, 0, 0]
ny = [0, 0, 1, -1]

table = [[10000]*m for _ in range(n)]
table[0][0] = 0

queue = deque([[0,0]])

while queue:
    x, y = queue.popleft()
    for i in range(4):
        dx = x + nx[i]
        dy = y + ny[i]
        if 0 <= dx < n and 0 <= dy < m:
            if table[x][y] + n_list[dx][dy] < table[dx][dy]:
                queue.append([dx, dy])
                table[dx][dy] = table[x][y] + n_list[dx][dy]

print(table[n-1][m-1])