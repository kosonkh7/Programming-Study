"""
두 자연수 N, K가 주어질 때, 두 연산 중 하나를 수행한다
1. N에서 1을 뺀다
2. N에서 K를 나눈다

2번 연산은 N이 K로 나누어 떨어질 때만.

N이 1이 되는 최소 연산 횟수를 구한다.

입력: N, K
출력: 최소 연산 횟수
"""

n , k = map(int, input().split())

result = 0

while (n > 1):
    if n%k ==0:
        n = (n // k)
    else:
        n -= 1
    result +=1

print(result)
