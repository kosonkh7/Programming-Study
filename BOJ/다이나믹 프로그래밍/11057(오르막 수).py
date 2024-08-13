"""
dp 테이블 구성할 때, 오르막 수의 각 끝자리를 반영하여 설계하였다.
"""

n = int(input())

dp = [[0]*10 for i in range(n+1)]

for i in range(0, 10):
    dp[1][i] = 1

if n>=2:
    for i in range(2, n+1):
        for j in range(0, 10):
                for k in range(0, j+1):
                    dp[i][j] += dp[i-1][k] # ex) dp[2][3] = dp[1][0] + dp[1][1] + dp[1][2] + dp[1][3]

print((sum(dp[n]))%10007)