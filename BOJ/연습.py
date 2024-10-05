n = int(input())

x, y = map(int, input().split()) # 시작
a, b = map(int, input().split()) # 도착지

x+=100
y+=100
a+=100
b+=100

dx = [1,-1,0,0] # 방향벡터
dy = [0,0,1,-1]

visited = [[False]*1000 for _ in range(1000)] # 방문 했는지
visited[x][y] = True

answer = 0

def dfs(q, r, s):
    global answer
    
    if s == n:
        if q == a and r == b:
            answer += 1
            return
        else:
            return

    else:
        for i in range(4):
            nx, ny = q+dx[i], r+dy[i]
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                dfs(nx, ny, s+1)
                visited[nx][ny] = False
        

dfs(x, y, 0)

print(answer)