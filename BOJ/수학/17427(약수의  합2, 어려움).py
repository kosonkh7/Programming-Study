"""
각각의 약수를 구하려면 시간 복잡도가 N^2로 아주 크기에 이 문제를 해결하는데 적합하지 않다고 한다.

N이하의 자연수 중에서 i를 약수로 갖는 수의 개수는 N/i라고 한다. 나 힌트 없이 이 규칙을 떠올릴 수 있었을까..
"""


#n = int(input())

# lst = [0] * 1000000
# lst[1] = 1
# lst[2] = 3

# for i in range(3, 11):
#     for j in range(2, i):
#         if i % j == 0:
#             lst[i] = i + lst[i//j]
#             break
#     if lst[i] == 0:
#         lst[i] = 1 + i

n = int(input())

sum = 0

for i in range(1, n+1):
    sum += (n//i)*i

print(sum)