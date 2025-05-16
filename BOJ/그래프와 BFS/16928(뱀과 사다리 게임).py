from collections import deque
n, m = map(int, input().split())

move = [0] * 101
for i in range(n+m):
    x, y = map(int, input().split())
    move[x] = y

dp = [999999] * 101

queue = deque([(1,0)])
dp[1] = 0

while queue:
    x, num = queue.popleft()
    if x == 100:
        break
    
    for i in range(1, 7):
        if x+i > 100:
            continue
        else:
            if move[x+i] == 0 and dp[x+i] > num+1:
                queue.append((x+i, num+1))
                dp[x+i] = num+1
            elif move[x+i] != 0:
                if dp[move[x+i]] > num+1:
                    queue.append((move[x+i], num+1))
                    dp[move[x+i]] = num+1

print(dp[100])