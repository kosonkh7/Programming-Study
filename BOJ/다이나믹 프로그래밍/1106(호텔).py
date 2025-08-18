"""
적어도 c명 올리기 위한 최솟값 (1000보다 작은 값)
n개 줄에 (비용, 고객 수) 입력 <- 둘 다 100보다 작은 값

그렇다면 가능한 고객 수부터..?

dp[x] <- n 최대인 20번씩 다 해봐도 시간 복잡도 널널할 듯

적어도 c명 늘리기 위한 최솟값이므로 dp를 널널하게 잡는 것이 중요할 듯
"""
c, n = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
n_list.sort(key=lambda x: [x[1], x[0]])

dp = [-1] * (c+101)
for x, y in n_list:
    dp[y] = x

for i in range(1, c+101):
    for x, y in n_list:
        if y >= i:
            break
        elif dp[i-y] == -1: 
            continue
        elif dp[i] == -1:
            dp[i] = dp[y] + dp[i-y]
        else:
            dp[i] = min(dp[i], dp[y] + dp[i-y])

answer = dp[c]
for i in range(c+1, c+101):
    if dp[i] != -1:
        answer = min(answer, dp[i])

print(answer)