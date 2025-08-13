"""
북동남서 0123
"""
n, m = map(int, input().split())
r, c, d = map(int, input().split())
n_list = []
visited = [] 

for i in range(n):
    tmp = list(map(int, input().split()))
    n_list.append(tmp)
    tmp_tf = []
    for t in tmp: # 벽이 있으면 방문 테이블도 방문 처리
        if t == 1:
            tmp_tf.append(True)
        else: tmp_tf.append(False)
    visited.append(tmp_tf) 

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1] 

answer = 0

def vacumm(x, y, d):
    global answer

    # 1번, 지금 칸 청소
    if not visited[x][y]:
        visited[x][y] = True
        answer += 1

    # 2번. 청소되지 않은 빈칸이 없는 경우
    if visited[x+1][y] == True and visited[x-1][y] == True and visited[x][y+1] == True and visited[x][y-1] == True:
        d_tmp = d - 2
        if d_tmp < 0: d_tmp += 4
        if n_list[x + dx[d_tmp]][y+dy[d_tmp]] == 1:
            return -1, -1, d
        else:
            return x + dx[d_tmp], y+dy[d_tmp], d
    
    # 3번. 반회전하면서 빈칸 있으면 한 칸 전진
    else:
        for i in range(1, 5):
            d_tmp = d - i
            if d_tmp < 0: d_tmp += 4
            if visited[x + dx[d_tmp]][y+dy[d_tmp]] == False:
                return x + dx[d_tmp], y+dy[d_tmp], d_tmp
            else: 
                continue

while r != -1 and c != -1:
    r, c, d = vacumm(r, c, d)

print(answer)