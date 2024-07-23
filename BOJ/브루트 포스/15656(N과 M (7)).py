n, m = map(int, input().split())

n_list = list(map(int, input().split()))

from itertools import product

answer = list(product(sorted(n_list), repeat=m))

for i in range(len(answer)):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()