# 1931 회의실 배정
# 하나의 회의실에 최대 몇 개 회의 배정 가능한가.

n = int(input())
n_list = []

for _ in range(n):
    x = list(map(int, input().split()))
    n_list.append(x)

n_list.sort(key=lambda x:[x[1], x[0]])

answer = 1
c = n_list[0][1]
for i in range(1, n):
    if n_list[i][0] >= c:
        c = n_list[i][1]
        answer += 1

print(answer)