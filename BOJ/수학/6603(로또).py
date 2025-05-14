from itertools import combinations

while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        break
    else:
        k = tmp[0]
        k_list = tmp[1:]

        for i in combinations(k_list, 6):
            for j in i:
                print(j, end=' ')
            print()

        print()

