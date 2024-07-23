n, m = map(int, input().split())

n_list = list(map(int, input().split()))

from itertools import combinations

answer = list(combinations(sorted(n_list), m))

for i in range(len(answer)):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()