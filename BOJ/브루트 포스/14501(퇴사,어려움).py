"""
다시 풀기.
"""
n = int(input())
schedule = [list(map(int, input().split())) for i in range(n)]
dp = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i+schedule[i][0], n+1):
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]
        print(dp)

print(dp[n])


"""
위 코드는 바텀업 방식.
i 번째 까지 일했을 때 최대 수익
j는 i번째까지 상담 진행했을 때 "상담 가능한 모든 날짜". 즉, i+상담기간부터 마지막 날까지이다.
그리고 j를 기준으로 상담을 진행했을 때 얻는 최대 수익을 저장 

7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
"""
