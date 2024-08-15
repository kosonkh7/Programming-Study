from copy import deepcopy

n = int(input())

triangle = [[0]*n for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        triangle[i][j] = line[j]

dp = deepcopy(triangle)

for i in range(n-1): 
    for j in range(i+1):
        x = triangle[i+1][j] + triangle[i][j]
        dp[i+1][j] = max(dp[i+1][j], x)
        y = triangle[i+1][j+1] + triangle[i][j]
        dp[i+1][j+1] = max(dp[i+1][j+1], y)
    triangle[i+1] = deepcopy(dp[i+1])

answer = max(map(max, dp))

print(answer)

