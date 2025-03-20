"""
B가 먼저 움직여야 A가 움직일 공간 확보 가능
방향벡터 정의하고, 하나씩 움직이는 함수 만들기

"""
from collections import deque
from copy import deepcopy

answer = -1
n, m = map(int, input().split())

n_list = []
for i in range(n):
    n_list.append(list(input()))

# 방문 테이블 -> 4차원 (A좌표랑 B좌표 모두 담게)
visited = [[[[False]* m for _ in range(n)]] * m for _ in range(n)]

# 처음 위치 찾기
for i in range(n):
    for j in range(m):
        if n_list[i][j] == 'R':
            r_loc = [i, j]
        if n_list[i][j] == 'B':
            b_loc = [i, j]

visited[r_loc[0]][r_loc[1]][b_loc[0]][b_loc[1]] = True

# 방향벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# r좌표, b좌표, 시도 횟수 
queue = deque([[r_loc[0], r_loc[1], b_loc[0], b_loc[1], 0, n_list]])

while queue:
    rx, ry, bx, by, num, new_list = queue.popleft()
    
    if num >= 10:
        continue

    elif answer >= 0:
        break
    
    else: 
        for i in range(4):
            if answer >= 0:
                break
            b_stop = False # B가 구멍에 들어가면 True, 이땐 queue에 넣어주지 않는다.
            r_stop = False # R이 구멍에 들어갔을 때 True

            newnew_list = deepcopy(new_list)

            while True:
                rnx = rx + dx[i]
                rny = ry + dy[i]
                bnx = bx + dx[i]
                bny = by + dy[i]

                # 둘 다 이동할 곳이 없으면 중지
                if newnew_list[rnx][rny] != '.' and newnew_list[bnx][bny] != '.' and newnew_list[rnx][rny] != 'O' and newnew_list[bnx][bny] != 'O':
                    break
                
                # 1. B구멍에 들어가면 이 경우는 없앰
                if newnew_list[bnx][bny] == "O":
                    b_stop = True
                    break
                # B 옆이 .이면 이동 -> 스왑 방식으로 이동
                elif newnew_list[bnx][bny] == ".": 
                    newnew_list[bnx][bny], newnew_list[bx][by] = newnew_list[bx][by], newnew_list[bnx][bny]
                    bx, by = bnx, bny
                
                # 2. R 구멍에 이미 들어갔으면 이동 없이 넘어감 
                if r_stop == True:
                    continue
                # 옆이 .이면 이동 -> 스왑 방식으로 이동
                elif newnew_list[rnx][rny] == ".": 
                    newnew_list[rnx][rny], newnew_list[rx][ry] = newnew_list[rx][ry], newnew_list[rnx][rny]
                    rx, ry = rnx, rny
                elif newnew_list[rnx][rny] == "O":
                    newnew_list[rx][ry] = '.'
                    r_stop = True
                    rx, ry = rnx, rny
            
            if b_stop==True: 
                continue
            elif r_stop==True: 
                answer = num + 1
                break
            elif visited[rx][ry][bx][by] == True:
                continue
            else:
                visited[rx][ry][bx][by] = True
                queue.append([rx, ry, bx, by, num+1, newnew_list])
                print(queue)

        
print(answer)

