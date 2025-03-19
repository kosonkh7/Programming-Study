from itertools import permutations
from collections import deque

# 입력값이 몇이든 scv 3개로 가정
n = int(input())
if n==3:
    n_list = list(map(int, input().split()))
    n_list.sort(reverse=True)
elif n == 2:
    n_list = list(map(int, input().split()))
    n_list.append(0)
    n_list.sort(reverse=True)
else:
    n_list = []
    n_list.append(int(input()))
    n_list.append(0)
    n_list.append(0)
    n_list.sort(reverse=True)

# 범위 61로 해도 되는데
dp = [[[99999]*100 for i in range(100)] for j in range(100)]  # 3차원 리스트 만들기
dp[n_list[0]][n_list[1]][n_list[2]] = 0

# 뮤탈이 공격할 수 있는 경우의 수
attack_case = list(permutations([9, 3, 1]))

queue = deque()
queue.append((n_list[0], n_list[1], n_list[2]))
# 꼭 필요 없이 바로 출력해도 될 듯!!!!!
answer = 99999

while queue:
    x, y, z = queue.popleft()

    if x <= 0 and y <= 0 and z <= 0:
        answer = min(dp[x][y][z], answer) # 그냥 여기서 break 해도 될 듯

    else:
        for i, j, k in attack_case:
            nx, ny, nz = max(0, x - i), max(0, y - j), max(0, z - k)
            if dp[nx][ny][nz] > dp[x][y][z] + 1:
                dp[nx][ny][nz] = dp[x][y][z] + 1
                queue.append((nx, ny, nz))

print(answer)