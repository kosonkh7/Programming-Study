l, c = map(int, input().split())
x_list = input().split()
c_list = []
c_a = []
c_b = []

for x in sorted(x_list):
    c_list.append(x)
    if x in ['a', 'e', 'i', 'o', 'u']:
        c_a.append(x)
    else:
        c_b.append(x)

from itertools import combinations

arr = list(combinations(c_list, l))

for i in range(len(arr)):
    a, b = 0, 0
    for j in range(l):
        if arr[i][j] in c_a:
            a+=1
        else:
            b+=1
    if a>=1 and b>=2:
        for j in range(l):
            print(arr[i][j], end="")
        print()
    else:
        continue


