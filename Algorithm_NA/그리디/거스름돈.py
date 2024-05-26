"""
입력값: 거슬러줘야할 돈 N (단, N은 10의 배수)
출력값: 최소 동전 개수
"""

n = int(input())

sum = 0

sum += (n // 500)
n = (n % 500)

sum += (n // 100)
n = (n % 100)

sum += (n // 50)
n = (n % 50)

sum += (n // 10)
n = (n % 10)

print(sum)