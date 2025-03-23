from collections import deque

a, b = map(int, input().split())
answer = -1

queue = deque([(a, 1)])

while queue:
    x, num = queue.popleft()
    
    if x == b:
        answer = num
        break

    if x * 2 <= b:
        queue.append((x*2, num+1))

    if x * 10 + 1 <= b:
        queue.append((x * 10 + 1, num+1))


print(answer)
    
    