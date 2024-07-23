n, m = map(int, input().split())

temp = []

for i in range(1, n+1):
    temp.append(i)

from itertools import product

comb = list(product(temp, repeat=m))

for i in range(len(comb)):
    for j in range(m):
        print(comb[i][j], end=' ')
    print()