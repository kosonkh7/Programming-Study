"""
location이라는 쓸데 없는 리스트 정의해서 코드가 복잡해짐
다른 사람 코드 보니 방문 리스트 없이도 풀었던데, 난 잘 쓴 것 같음
"""

from collections import deque

n, m = map(int, input().split())
n_list = [] # 입력값 받을 이중 리스트
dx = [1, -1, 0, 0] # 방향벡터 정의
dy = [0, 0, 1, -1]

for _ in range(n):
    n_list.append(list(input()))

location = [[0]*m for _ in range(n)] # 두 동전의 위치를 담을 리스트, 1이면 해당 위치에 동전 있다는 의미인데, 이거 아예 필요 없을 것 같은데? 
queue = [] # 큐에 동전 위치 담아주기 위함.
for i in range(n):
    for j in range(m):
        if n_list[i][j] == 'o':
            location[i][j] = 1
            queue.append(i)
            queue.append(j)


queue.append(0) # 큐에 이동 횟수 담아줌. 초기값 0
queue.append(location)
queue.append([]) # 큐에 방문 리스트 담아줌. 초기값 빈 리스트
queue = deque([queue])

answer = 999999
while queue: # BFS로 구현
    if answer != 999999: # 정답 찾았으면 BFS 탈출
        break

    i1, j1, i2, j2, num, loc, visited = queue.popleft()
    visited.append([i1, j1, i2, j2]) # 방문 처리
    drop = 0

    for i in range(4):
        drop = 0
        nx1 = i1 + dx[i]
        ny1 = j1 + dy[i]
        nx2 = i2 + dx[i]
        ny2 = j2 + dy[i]
        
        if nx1 < 0 or nx1 >= n or ny1 < 0 or ny1 >= m: # 떨어지는 건지 확인
            drop += 1
        elif n_list[nx1][ny1] == '#': # 벽에 막히면 제자리
            nx1, ny1 = i1, j1
        else:
            if n_list[nx1][ny1] != '#': # 벽에 안 막혔으면 움직여줌
                loc[nx1][ny1] += 1
                loc[i1][j1] -= 1

        if nx2 < 0 or nx2 >= n or ny2 < 0 or ny2 >= m: # 두 번째 동전도 같은 원리로 이동
            drop += 1
        elif n_list[nx2][ny2] == '#':
            nx2, ny2 = i2, j2
        else:
            if n_list[nx2][ny2] != '#':
                loc[nx2][ny2] += 1
                loc[i2][j2] -= 1

        if drop == 1: # 하나만 떨어트렸으면 정답 찾음
            answer = num+1
        elif drop == 0 and [nx1, ny1, nx2, ny2] not in visited and num+1 < 10: # 아무 것도 안 떨어트렸으면 큐에 담음
            queue.append([nx1, ny1, nx2, ny2, num+1, loc, visited])
            

if answer == 999999: # 정답 없으면 -1 출력
    print(-1)
else:
    print(answer)

