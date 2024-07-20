"""
카드가 i개 포함된 카드팩의 가격은 Pi원이다.

첫째 줄에 민규가 구매하려고 하는 카드의 개수 N이 주어진다. (1 ≤ N ≤ 1,000)

둘째 줄에는 Pi가 P1부터 PN까지 순서대로 주어진다. (1 ≤ Pi ≤ 10,000)

N개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값을 구하는 프로그램을 작성하시오. 
"""

n = int(input())
p_list = list(map(int, input().split()))
p_list.insert(0, 0)

dp = [0] * (n+1)
dp[1] = p_list[1]
dp[2] = max(p_list[1]+p_list[1], p_list[2])

def aaa(n):
    answer = 0
    for i in range(1, n//2+1):
        now = dp[i] + dp[n-i]
        answer = max(answer, now)
    return answer

for i in range(3, n+1):
    dp[i] = max(aaa(i), p_list[i])

print(dp[n])