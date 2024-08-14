"""
포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
연속으로 놓여 있는 3잔을 모두 마실 수는 없다.

점화식을 올바르게 세워야 한다.

초기 점화식
1. i번째 먹고 i-1번째 먹지 않는다.
2. i, i-1번째 먹고 i-2번째 먹지 않는다.
틀린 이유 -> i번째를 안 먹는 것을 고려하지 않았고, 최대 한 잔만 건너 뛰는게 최선이라 생각했는데, 
ex) 10 10 1 1 50 50 과 같은 케이스를 올바르게 담지 못한다.

보완한 점화식
1. i번째 먹고 i-1번째 먹지 않고, i-2번째를 먹는다
2. i, i-1번째 먹고 i-2번째 먹지 않는다.
3. i번째를 먹지 않는다.
"""

n = int(input())
n_list = []
for i in range(n):
    n_list.append(int(input()))

dp = [0]*n

dp[0] = n_list[0]

if n > 1:
    dp[1] = n_list[0]+n_list[1]

if n > 2:
    dp[2] = max(n_list[2]+n_list[1], n_list[2]+n_list[0], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-3]+n_list[i-1]+n_list[i], dp[i-2]+n_list[i])

print(dp[n-1])



"""
초기 코드
n = int(input())
n_list = [0]
for _ in range(n):
    a = int(input())
    n_list.append(a)

dp = [[0]*2 for _ in range(n+1)]
dp[1][0], dp[1][1] = n_list[1], n_list[1]

answer = 0

if n >= 2:
    for i in range(2, n+1):
        dp[i][0] = n_list[i] + dp[i-2][1]
        dp[i][1] = n_list[i] + dp[i-1][0]

    for i in range(1, n+1):
        for j in range(2):
            answer = max(answer, dp[i][j])

if n == 1:
    answer = n_list[1]

print(answer)

"""