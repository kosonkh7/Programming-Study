"""

"""

n =  int(input())
n_list = list(map(int, input().split()))
n_list.insert(0, 0)
dp = [10001]*(n+1)

dp[1] = n_list[1]
dp[2] = min(n_list[2], n_list[1]*2)

for i in range(3, n+1):
    for j in range(1, i//2+1):
        dp[i] =  min(dp[i], dp[j] + dp[i-j])
    dp[i] = min(dp[i], n_list[i])

print(dp[n])