"""
특정 지점 기준으로 왼쪽에서 오는 파이프, 대각선에서 오는 파이프, 위에서 오는 파이프 3가지로 구분하여 dp테이블 설계

shape(dp) = (n, n, 3)

그림으로 그려보면 패턴이 보였다

벽 정보는 n_list에 담고, 대각선 관련해서 벽 조건 처리.
"""

n = int(input())

# 왼쪽, 대각선, 위쪽
dp = [[[0]*3 for _ in range(n)] for _ in range(n)]

n_list = [list(map(int, input().split())) for _ in range(n)]

dp[0][1][0] = 1

for i in range(n):
    for j in range(1, n):
        if n_list[i][j] == 1:
            continue
        if i == 0 and j == 1:
            continue
        else:
            # 왼쪽에서 오는 거
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]

            # 대각선에서 오는 거
            if i-1 >= 0 and n_list[i-1][j] == 0 and n_list[i][j-1] == 0:
                dp[i][j][1] = sum(dp[i-1][j-1])

            # 위에서 오는 거
            if i-1 >= 0:
                dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]


print(sum(dp[n-1][n-1]))