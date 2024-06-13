"""
배열의 크기 N
숫자 더해지는 횟수 M
한 원소가 K번 초과하여 더해질 수 없다.

입력: 첫째줄에 N, M, K (모두 정수), 둘째줄에 N개의 정수
출력: 합 
"""

n, m, k = map(int, input().split())

narray = list(map(int, input().split()))

narray.sort(reverse=True)

x = m // k
y =  m % k

sum = 0

if m > k:
    for i in range(x):
        for j in range(k):
            sum += narray[i]

    for i in range(y):
        sum += narray[x]

elif m == k:
    sum += narray[0]*k

print(sum)