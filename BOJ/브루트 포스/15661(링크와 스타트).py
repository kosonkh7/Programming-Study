"""
1. 팀 인원 수 나누는 경우 계산
2. 정해진 인원 수 별로 팀 나누는 경우
3. 나눠진 팀 별로 점수 합산

-> 처음에 시간 초과 떴는데, 형변환 함수(list(), set() 등)만 최소화 해주니 간신히 통과하여 맞춘 느낌이다.
combinations도 시간 복잡도가 높지만, 형변환 함수가 생각보다 시간 복잡도를 잡아먹는다고 하더라.
"""

from itertools import combinations

n = int(input())
n_list  = set([i for i in range(n)])

arr = []
for _ in range(n):
    arrlist = list(map(int, input().split()))
    arr.append(arrlist)

answer = 999999999999

# 1. 팀 인원 수 나누는 경우 계산
for x in range(1, n//2+1):
    # 2. 정해진 인원 수 별로 팀 나누는 경우
    for xteam in combinations(n_list, x):
        yteam = n_list - set(xteam)

        xscore = 0
        yscore = 0
        # 3. 나눠진 팀 별로 점수 합산
        if x == 1:
            continue
        else:
            for i, j in combinations(xteam, 2):
                xscore += (arr[i][j] + arr[j][i])

        for i, j in combinations(yteam, 2):
            yscore += (arr[i][j] + arr[j][i])
        
        answer = min(answer, abs(xscore-yscore))

print(answer)