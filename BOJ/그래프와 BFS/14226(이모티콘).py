"""
1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
3. 화면에 있는 이모티콘 중 하나를 삭제한다.

변수: 화면, 클립보드, 시간
"""

from collections import deque

target = int(input())

screen = 1
clip = 0
time  = 0
visited = [[False] * (target+1) for _ in range(target+1)]

def bfs(screen, clip, time):
    queue = deque([(screen, clip, time)])
    
    while queue:
        s, c, t = queue.popleft()
        if s == target:
            return t
        
        visited[s][c] = True

        if s != c and visited[s][s]==False:
            queue.append((s, s, t+1))
        
        if c != 0 and s+c <= target and visited[s+c][c]== False:
            queue.append((s+c, c, t+1))   
        
        if s-1 > 1 and visited[s-1][c] == False:
            queue.append((s-1, c, t+1))


answer = bfs(screen, clip, time)

print(answer)

"""
규칙 파악은 금방 하였으나, 시간 초과와 메모리 초과에 애먹었다.

"""