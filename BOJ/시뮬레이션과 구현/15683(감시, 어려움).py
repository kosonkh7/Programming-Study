"""
문제는 이해했는데, 워낙 복잡해서 미뤄둠. 꼭 다시 풀기. 못 풀 정도 아님

"""
n, m = map(int, input().split())
n_list = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cctv = []
answer = 0

for i in range(n):
    for j in range(m):
        if n_list[i][j] != 0 and n_list[i][j] != 6:
            cctv.append([n_list[i][j], i, j])
        elif n_list[i][j] == 0:
            answer += 1

print(cctv)

# def dfs(num, n_list):s