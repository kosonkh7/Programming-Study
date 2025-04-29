n, m = map(int, input().split())

n_list = [list(map(int, input().split())) for _ in range(n)]

print(n_list)

answer = n*m


# 일단 전체에서 육면을 바라보았을 때 면적
tmpsum = 0
for i in range(n):
    tmpx = 0
    for j in range(m):
        tmpx = max(tmpx, n_list[i][j])
    tmpsum += tmpx

answer += tmpsum

tmpsum = 0
for i in range(m):
    tmpx = 0
    for j in range(n):
        tmpx = max(tmpx, n_list[j][i])
    tmpsum += tmpx

answer += tmpsum

answer *= 2

# 이제 올록 볼록한 구조 찾기
"""
V자로 내려가다 올라가는 구조를 복잡하게 찾으려고 했는데

이전 블럭에 비해 증가하면 하나씩 키워주는 식으로 해결이 되는 것 같다?

다시 풀기 (코드 구조 처음부터 다시 짜기)
"""


print(answer)