from collections import deque

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

"""
메모리 초과 나는데 아마도 정답 풀이일 것
큐가 계속해서 길어지기 때문에 메모리 초과 발생하는 것으로 보임.
이중 반복문을 통해 dp 계속하여 업데이트 해나가면 풀리는 단순한 방식.

queue = deque([[0, 0]])

while queue:
    x, y = queue.popleft()

    if x + n_list[x][y] < n:
        dp[x + n_list[x][y]][y] += 1

        if x + n_list[x][y] == n-1 and y == n-1:
            continue
        else:
            queue.append([x + n_list[x][y], y])

    if y + n_list[x][y] < n:
        dp[x][y + n_list[x][y]] += 1

        if x == n-1 and y + n_list[x][y] == n-1:
            continue
        else:
            queue.append([x, y + n_list[x][y]])

print(dp[n-1][n-1])
"""