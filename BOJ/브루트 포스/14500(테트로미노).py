"""
세로 크기 N과 가로 크기 M이 주어진다. (4 ≤ N, M ≤ 500)
둘째 줄부터 N개의 줄에 종이에 쓰여 있는 수가 주어진다. 
i번째 줄의 j번째 수는 위에서부터 i번째 칸, 왼쪽에서부터 j번째 칸에 쓰여 있는 수이다. 
입력으로 주어지는 수는 1,000을 넘지 않는 자연수이다.

숫자 판 위에 테트로미노 하나를 올려서 합의 최대값을 구하는 것 (테트로미노는 다섯 가지, 회전시켜서 모양이 다른 것까지 총 19가지 존재한다)
각각 반복문 돌고 최대값 구하는 것으로 시도
"""

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

maxsum = 0

for i in range(n):
    for j in range(m-3):
        x = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i][j+3]
        maxsum = max(x, maxsum)

for i in range(n-3):
    for j in range(m):
        x = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+3][j]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i+2][j+1]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j] + lst[i+1][j] + lst[i+2][j] + lst[i][j+1]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j] + lst[i+1][j+1] + lst[i+2][j+1] + lst[i][j+1]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j+1] + lst[i+1][j+1] + lst[i+2][j+1] + lst[i+2][j]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j+1] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j+1]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-1):
        x = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i][j+1]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j+1]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i+1][j] + lst[i+1][j+1] + lst[i+1][j+2] + lst[i][j+1]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i+1][j] + lst[i+1][j+1] + lst[i+1][j+2] + lst[i][j+2]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j+2]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i][j] + lst[i+1][j+1] + lst[i+1][j+2] + lst[i+1][j]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i][j] + lst[i][j+1] + lst[i][j+2] + lst[i+1][j]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j+1]
        maxsum = max(x, maxsum)

for i in range(n-2):
    for j in range(m-1):
        x = lst[i][j+1] + lst[i+1][j] + lst[i+1][j+1] + lst[i+2][j]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i][j] + lst[i][j+1] + lst[i+1][j+1] + lst[i+1][j+2]
        maxsum = max(x, maxsum)

for i in range(n-1):
    for j in range(m-2):
        x = lst[i+1][j] + lst[i][j+1] + lst[i+1][j+1] + lst[i][j+2]
        maxsum = max(x, maxsum)


print(maxsum)