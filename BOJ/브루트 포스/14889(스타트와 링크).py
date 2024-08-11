"""
조합과 순열을 적절하게 활용하여 풀고자 하였다.

1. n명을 2그룹으로 나누는 경우의 수 (n)C(n/2)
2. 그룹 별로 합을 계산하는 경우 (n/2)P(2) 경우 합 계산

"""

from itertools import combinations, permutations

n = int(input())
n_list = [i for i in range(n)]
arr = [list(map(int, input().split())) for _ in range(n)]

answer = 100000000

divide_group = list(combinations(n_list, n//2)) # 2그룹으로 나눔

for a in range(len(divide_group)//2): # 중복 계산을 방지하고자 인덱스를 절반까지 설계
    groupa = divide_group[a]
    groupb = set(n_list) - set(groupa)

    suma = 0
    sumb = 0

    for i, j in permutations(groupa, 2): # 한 그룹에서 2명 뽑는 순열 계산
        suma += arr[i][j]
    
    for i, j in permutations(groupb, 2):
        sumb += arr[i][j]

    answer = min(answer, abs(suma-sumb))


print(answer)



"""
다른 분들은 주로 백트래킹을 활용해서 풀었더라. 
아직 백트래킹을 이해하지 못했는데 공부할 필요성을 느낀다면 해볼 것
"""