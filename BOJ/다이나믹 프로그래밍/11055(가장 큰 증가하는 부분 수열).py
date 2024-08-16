n = int(input())
a = [0]
x = list(map(int, input().split()))
a.extend(x)


# i번째 값을 수열의 마지막 값으로 하는 수열의 합을 dp테이블에 담음
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    max_index = 0
    for j in range(i-1, -1, -1): # i-1번째 부터 거꾸로 가면서 조회
        if a[i] > a[j]: # 만약에 증가하고 있는 수열이 만족한다면
            if dp[max_index] < dp[j]: # 합이 최대가 되는 이전 수열의 인덱스를 찾아서
                max_index = j
    dp[i] = a[i] + dp[max_index] # i값과 더해주어 dp테이블에 저장

print(max(dp))