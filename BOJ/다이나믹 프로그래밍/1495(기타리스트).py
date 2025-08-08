# dp 문제라는데 bfs로 풀었다...

n, s, m = map(int, input().split())
n_list = list(map(int, input().split()))

from collections import deque

queue = deque([[s, 0]])

answer = -1
dx = [1, -1]
while queue:
    now, index = queue.popleft()
    if index == n:
        answer = max(answer, now)
    else:
        for i in range(2):
            tmp = now + n_list[index]*dx[i]
            if 0 <= tmp <= m and [tmp, index+1] not in queue: # queue 길이 안 줄이면 메모리 초과.
                queue.append([tmp, index+1])

print(answer)