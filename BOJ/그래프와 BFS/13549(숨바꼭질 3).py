"""
1. 그냥 BFS로 풀어봤는데 가뿐히 틀림
2. 순간이동한 칸은 queue의 앞쪽에 되도록 이중 while문을 이용해 보았는데 시간 초과 발생
3. appendleft 문법을 알게 된 후에 복잡한 이중 반복문 없이 문제 해결

-> 시행착오 없이 문제 포인트를 캐치할 안목이 아직은 부족하다.
"""

from collections import deque

n, k = map(int, input().split())
visited = [False]*(100001)

def bfs():
    queue = deque([(n, 0)])
    visited[n] = True      

    while queue:
        now, num = queue.popleft()

        if now == k:
            return num
        
        if 0 <= now*2 <= 100000 and visited[now*2]==False:
            queue.appendleft((now*2, num))
            visited[now*2] = True

        if 0 <= now+1 <= 100000 and visited[now+1]==False:
            queue.append((now+1, num+1))
            visited[now+1] = True

        if now-1 >= 0 and visited[now-1]==False:
            queue.append((now-1, num+1))
            visited[now-1] = True

answer = bfs()

print(answer)



"""
def bfs():
    queue = deque([(n, 0)])
    #visited[n] = True      

    while queue:
        now, num = queue.popleft()
        visited[now] = True

        if now == k:
            return num
        
        x = now * 2 
        if x > 100000:
            continue
        else:
            while x <= 100000:
                if x > 100000:
                    break
                elif x == k:
                    return num
                elif visited[x]==True:
                    break
                else:
                    queue.append((x, num))
                    visited[x] = True
                    x *= 2

        if now+1 <= 100000 and visited[now+1]==False:
            queue.append((now+1, num+1))

        if now-1 >= 0 and visited[now-1]==False:
            queue.append((now-1, num+1))

answer = bfs()

print(answer)
"""