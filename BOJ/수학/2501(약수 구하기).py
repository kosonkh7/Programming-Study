"""
첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다. 만일 N의 약수의 개수가 K개보다 적어서 K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.
"""

n, k = map(int, input().split())

answer = 0
i = 0 # 계속 증가하는 나눌 수
x = 0 # 몇 번째 약수인지

while i <= n:
    i += 1

    if n % i == 0:
        x += 1
    
    if x == k:
        answer = i
        break

print(answer)