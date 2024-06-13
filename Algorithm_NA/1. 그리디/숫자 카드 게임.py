"""
N x M 크기의 자연수로 이뤄진 배열
규칙에 맞게 수를 출력

입력: 첫째 줄엔 N, M, 둘째 줄엔 배열
출력: 각 행마다 가장 작은 수 중에서 가장 큰 수를 출력
"""

n, m = map(int, input().split())

narray = [list(map(int, input().split())) for _ in range(n)]

result = 0

# 각 행마다 가장 작은 수 중에서, 가장 큰 값을 result에 저장
for i in range(n):
    if result < min(narray[i]):
        result = min(narray[i])

print(result)
