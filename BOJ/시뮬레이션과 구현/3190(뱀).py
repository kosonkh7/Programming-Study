from collections import deque

n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
k_list = list(list(map(int, input().split())) for _ in range(k)) # 사과 위치
l = int(input()) # 뱀 방향 변환 횟수
l_list = list(list(input().split()) for _ in range(l)) # 뱀 변환 규칙
li = 0 # 변환 인덱스

visited = [[False]*n for _ in range(n)] # 방문 테이블 -> 뱀이 걸쳐져 있는 위치
visited[0][0] = True
n_list = [[0]*n for _ in range(n)]  # 보드
for i in range(k):                  # 사과 위치 명시
    x, y = k_list[i][0], k_list[i][1]
    n_list[x-1][y-1] = 1
tail = deque([[0,0]]) # 꼬리가 짧아질 때 방문 테이블도 다시 True로 바꿈

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
di = 0 # 뱡향벡터 인덱스, 0, 1, 2, 3

x, y = 0, 0 # 머리 위치
answer = 0
while True:
    answer += 1
    nx, ny = x+dx[di], y+dy[di]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == True: # 벽이나 자기 몸에 부딪히면
        break

    elif n_list[nx][ny] == 1: # 사과 먹으면
        n_list[nx][ny] = 0 # 사과 먹고
        visited[nx][ny] = True # 몸 길어지고
        tail.append([nx, ny]) # 꼬리에 추가
        x, y = nx, ny # 머리 위치 수정

    elif n_list[nx][ny] == 0: # 사과 못 먹으면
        visited[nx][ny] = True # 몸 길어지고
        tail.append([nx, ny]) # 꼬리에 추가
        tmpx, tmpy = tail.popleft() # 
        visited[tmpx][tmpy] = False # 원래 꼬리 짧아지기
        x, y = nx, ny # 머리 위치 수정

    if li < l and l_list[li][0] == str(answer): # 회전할 타이밍이면
        if l_list[li][1] == 'D': # 오른쪽이라면
            di += 1
            if di == 4:
                di = 0
        else: # 왼쪽이라면
            di -= 1
            if di == -1:
                di = 3
        
        li += 1

print(answer)
