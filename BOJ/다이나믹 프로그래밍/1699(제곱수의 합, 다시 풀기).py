n = int(input())

visited = [False] * (n+1)
dp = [0] * (n+1)
dp[1] = 1 

if n > 1:
    x = 1
    for i in range(1, n+1):
        if i == x**2:
            dp[i] = 1
            x += 1
        else:
            dp[i] = dp[(x-1)**2] + dp[i-(x-1)**2]

print(dp[n])


"""
12일 때
dp[9]+dp[3] > dp[4] + dp[4] + dp[4]

이걸 고려해야한다. 
구글링 해보니 내 코드처럼 x를 사용하지 않고, 
이중 반복문을 사용하여 더 많은 경우를 비교하고, 이때 최소값이 있으면 업데이트 하는 방식으로 진행하더라. 
"""