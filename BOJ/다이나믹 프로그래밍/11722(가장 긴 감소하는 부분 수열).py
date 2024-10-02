"""

"""


n = int(input())
tmp = list(map(int, input().split()))
n_list = []
for i in range(n-1, -1, -1):
    n_list.append(tmp[i])

# 가장 긴 증가하는 부분 수열 문제로 변환 <= 꼭 그러지 않고 반대로만 하면 되는데, 생각하기 편한대로 풀었다.
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    x = 0
    for j in range(i):
        if n_list[j] < n_list[i]:
            x = max(x, dp[j])
    dp[i] = x + 1

# print(n_list)    
# print(dp)

print(max(dp))