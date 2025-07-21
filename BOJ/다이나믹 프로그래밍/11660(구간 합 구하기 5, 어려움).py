# https://www.acmicpc.net/problem/11660
# 시간 초과!!!!

"""
import sys 
input = sys.stdin.readline
n, m = map(int, input().split())

n_list = list(list(map(int, input().split())) for _ in range(n))

이렇게 풀면 시간 초과!!!!!! 리스트 슬라이싱 연산도 줄여야 했다.
for _ in range(m):
    sum_ = 0
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1-1, x2):
        sum_ += sum(n_list[i][y1-1:y2])
    print(sum_)
"""

"""
이것도 느림...
import sys 
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (N+1) for _ in range (N+1)]

# 누적합 dp 계산(보텀업)
for i in range (1, N+1) :
    for j in range (1, N+1) :
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + arr[i-1][j-1]

# 원하는 구간 계산 
for _ in range (M) :
    x1, y1, x2, y2 = map(int, input().split())

    ans = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    print(ans)

"""
