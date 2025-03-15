# 시간복잡도 문제인지.. 안되는 이유를 모르겠다.

from itertools import combinations

def is_square(combination):
    is_true = True
    criterion = combination[1][1] - combination[0][1]
    if (combination[2][0] - combination[0][0]) != criterion:
        return False, criterion
    if (combination[3][1] - combination[2][1]) != criterion:
        return False, criterion    
    if (combination[3][0] - combination[1][0]) != criterion:
        return False, criterion      
    
    return is_true, criterion

n, m= map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]
answer = 0

points = [[] for _ in range(101)]

for i in range(n):
    for j in range(m):
        points[n_list[i][j]].append([i, j])

for i in range(1, 101):
    if len(points[i]) >= 4:
        points[i].sort()
        for combination in combinations(points[i], 4):
            is_true, criterion = is_square(combination)
            if is_true==True:
                answer = max(answer, (criterion+1)**2)

print(answer)