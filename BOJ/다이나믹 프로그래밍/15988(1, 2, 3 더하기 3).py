t = int(input())
t_list = []

for _ in range(t):
    a = int(input())
    t_list.append(a)

amax = max(t_list)

dp = [[0] for _ in range(amax+1)]
dp[1] = 1
dp[2] = 2
dp[3] = 4
dp[4] = 7

for i in range(5, amax+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009 # 처음부터 나머지로 dp에 저장 안하면 메모리 초과 발생

for i in t_list:
    print(dp[i])
