"""
아래 코드는 시간 복잡도가 커서 사용하지 못한다.
t = int(input())

for i in range(t):
    try:
        n = int(input())
    except:
        break
    sum = 0
    for i in range(1, n+1):
        sum += (n//i)*i
    print(sum)

f[x] -> x의 약수의 합
g[x] -> f[x]+f[x-1]+...f[1] = f[x] +g[x-1]

아래 방법으로 풀면 시간 복잡도 nlogn
설명: 약수인 것만 더해주는 방법

while문 -> 조화 급수에 비슷하기 때문에 대략적으로 nlogn의 시간복잡도 가진다.
"""

# DP 1로 초기화 -> 모두 약수로 1을 포함하므로
dp = [1]*(1000001)

# S: 값 누적 리스트
s = [0]*(1000001)
s[1] = 1
dp[1] = 1

for i in range(2, 1000001):
    j=1
    while i*j <= 1000000:
    	# i의 배수에 값 추가
        dp[i*j] += i
        j += 1
    s[i] = s[i-1] + dp[i]

# for i in range(1, 1000001):
# 	# 누적 값 계산
#     s[i] = s[i-1] + dp[i]

t = int(input())

for i in range(t):
    n = int(input())
    print(s[n])



"""
위 코드는 시간 초과고, 아래 코드는 시간 초과가 안 나는 이유를 모르겠다.
max = 1000000

M = [0 for i in range(max+1)] #누적합 g(x)를 담는 메모
m = [0 for i in range(max+1)] #해당 값의 약수의 합 f(x)를 담는 메모

for i in range(1,max+1):
    j = 1
    while i * j <= max: # i*j 값이 최대값이 넘지 않을 때까지
        m[i*j] += i
        j += 1
    M[i] = M[i-1] + m[i]

n = int(input())
divList = list()
for i in range(n):
    a = int(input())
    divList.append(a)
for i in divList:
    print(M[i])
"""

