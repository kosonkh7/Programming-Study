# 11404 플로이드
n = int(input()) # 도시 개수
m = int(input()) # 버스 개수

cost = [[10**9]*n for _ in range(n)]
for i in range(n):
    cost[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    cost[a-1][b-1] = min(cost[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(n):
    for j in range(n):
        if cost[i][j] == 10**9:
            cost[i][j] = 0
        if j != n-1:
            print(cost[i][j], end=' ')
        else:
            print(cost[i][j])