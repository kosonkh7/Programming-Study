"""
정사각형 개수
입력값: N
출력값: 길이가 N인 격자에서 정사각형의 개수

a1 = 1
a2 = 1+4
a3 = 1+4+9
a4 = 1+4+9+16
...
"""

n_list = [0] * 1000001

for i in range(len(n_list)):
    n_list[i] = i*i

n = int(input())

answer = 0

for i in range(n+1):
    answer += n_list[i]

print(answer)