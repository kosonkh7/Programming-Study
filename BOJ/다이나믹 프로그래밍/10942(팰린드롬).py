# 펠린드롬 -> 거꾸로 읽어도 같은 수열
# 점화식 세우는 것이 아직 익숙하지 않다.

n = int(input())
n_list = [0] + list(map(int, input().split()))
m = int(input())
# m_list = list(list(map(int, input().split()) for _ in range(m)))
# print(n_list)


dp = [[False] * (n+1) for _ in range(n+1)]

# 길이가 1일 때
for i in range(1, n+1):
    dp[i][i] = True

# 길이가 2일 때
for i in range(1, n):
    if n_list[i] == n_list[i+1]:
        dp[i][i+1] = True

# 길이가 3이상일 때
for length in range(3, n+1):
    for start in range(1, n - length + 2):
        end = start + length -1
        if n_list[start] == n_list[end] and dp[start+1][end-1]:
            dp[start][end] = True


for i in range(m):
    s, e = map(int, input().split())
    print(int(dp[s][e]))
    #print(int(dp[s][e]))







"""
초기에 작성한 방식
1. n^2로 시간 초과가 발생할 뿐 아니라
2. 수열의 길이가 짝수도 펠린드롬이 될 수 있다는 것을 놓쳤다 (1331)

dp = [1] * (n+1)
for i in range(1, n):
    num = 1
    while True:
        if i - num > 0 and i + num <= n and n_list[i-num] == n_list[i+num]:
            num += 1
            dp[i] = num
        else: 
            break

# print(dp)

for x, y in m_list:
    if (y+x) % 2 == 1:
        print(0)
    elif dp[(y+x) // 2] -1  >= (y-x) // 2:
        print(1)
    else:
        print(0)
"""
