n = int(input())

t_list = [0] # 기간
p_list  = [0] # 금액

for _ in range(n):
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

dp = [0] * (n+2)

# 거꾸로 dp 테이블 업데이트
for i in range(n, 0, -1):
    if i + t_list[i] - 1 > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], p_list[i] + dp[i+t_list[i]])

print(dp[1])