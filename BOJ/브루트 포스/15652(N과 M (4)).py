n, m = map(int, input().split())

temp = []

for i in range(1, n+1):
    temp.append(i)

from itertools import product

comb = list(product(temp, repeat=m))

answer_list =[]

for i in range(len(comb)):
    x = sorted(comb[i])
    if x not in answer_list:
        answer_list.append(x)

for i in range(len(answer_list)):
    for j in range(m):
        print(answer_list[i][j], end=' ')
    print()