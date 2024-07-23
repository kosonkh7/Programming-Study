# 메모리 초과가 난다. 백트래킹(DFS) 이용하면 해결되는 것 같다지만, 범위가 정수 8이하인데도 왜 초과가 나는 걸까

from itertools import product

n, m = map(int, input().split())

temp = []

for i in range(1, n+1):
    temp.append(i)

comb = list(product(temp, repeat=m))

#del temp
answer_list =[]

for i in range(len(comb)):
    if sorted(comb[i]) not in answer_list:
        answer_list.append(sorted(comb[i]))


for i in range(len(answer_list)):
    for j in range(m):
        print(answer_list[i][j], end=' ')
    print()