"""
n이 홀수면 무조건 0
3xn개 크기의 고유 모양 존재 (그림 그리면 이해 가능)
"""
n = int(input())

dp = [0] * 16
dp[0] = 1
dp[1] = 3 # 단위 블럭

for i in range(2, 16):
    dp[i] += dp[i-1] * dp[1] # 이전 블럭에 단위 블럭 붙이기
    for j in range(i-2, -1, -1): # 단위 블럭에 각 고유의 블럭 붙이는 경우 (중복 고려한 점화식)
        dp[i] += dp[j]*2

if n % 2 == 1:
    print(0)
else:
    print(dp[n//2])




"""
아래 코드 점화식을 잘 세웠다고 생각했는데,
고유 모양만으로 이뤄진 걸 반영하지 않아서 규칙이 어그러졌다.

n = int(input())

dp = [0] * 16

dp[1] = 3

for i in range(2, 16):
    dp[i] += 3**i
    for j in range(i-1, 0, -1): 
        dp[i] += 2*(3**(j-1))*j

#print(dp)

if n % 2 == 1:
    print(0)
else:
    print(dp[n//2])

"""