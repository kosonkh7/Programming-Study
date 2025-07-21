"""
50   30+10
30   50 + 50
0    0 + 50


dp 1, 2, 3행 각각
첫번째, 두번째, 둘다x 골랐을 때 각각 최대값 조합 업데이트

"""



t = int(input())

for x in range(t):
    n = int(input())
    n_list = [list(map(int, input().split())) for _ in range(2)]

    dp = list([0] * n for _ in range(3))
    dp[0][0], dp[1][0] = n_list[0][0], n_list[1][0] 

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1] + n_list[0][i], dp[2][i-1] + n_list[0][i])
        dp[1][i] = max(dp[0][i-1] + n_list[1][i], dp[2][i-1] + n_list[1][i])
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])

    print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))

# print(n_list)
# print(dp)