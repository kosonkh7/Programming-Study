n, m = map(int, input().split())

n_list = list(map(int, input().split()))

# for i in range(n):
#     n_list.append(int(input()))

from itertools import permutations

answer = list(permutations(n_list, m))

for i in range(len(answer)):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()