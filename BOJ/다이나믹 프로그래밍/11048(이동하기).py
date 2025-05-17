n, m = map(int, input().split())

dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(m-1):
    dp[0][i+1] =  dp[0][i+1] + dp[0][i]

for i in range(n-1):
    dp[i+1][0] =  dp[i+1][0] + dp[i][0]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = dp[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n-1][m-1])