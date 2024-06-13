"""
입력값: 배열 크기 n, 최대 교환 횟수 k, 배열 2개
출력값: 배열 합의 최대값
"""

n, k = map(int, input().split())

array1 = [map(int, input().split())]
array2 = [map(int, input().split())]

array1.sort()
array2.sort(reverse=True)

for i in range(k):
    if array1[i] < array2[i]:
        array1[i], array2[i] = array2[i], array1[i]
    else:
        break

for i in range(n):
    print(array1[i], end=' ')