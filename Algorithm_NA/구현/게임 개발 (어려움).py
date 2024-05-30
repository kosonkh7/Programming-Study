"""
육지: 0, 바다: 1 
캐릭터는 규칙에 따라 육지로만 이동할 수 있다
1. 좌로 방향 회전
2. 육지면 이동, 아니면 다시 좌로 회전
3. 한 바퀴 다 돌았는데 길이 없으면 뒤로 이동, 근데 뒤도 바다면 종료

입력값: 지도 크기 n, m / 캐릭터 위치 좌표, 방향 a, b, d / 지도 모양 n*m
출력값: 캐릭터가 방문한 칸의 수

d = [0, 1, 2, 3] (북 동 남 서)
0일 때 a-1
1일 때 b+1
2일 때 a+1
3일 때 b-1

방향 벡터와 그 인덱스를 적절하게 이용할 수 있는 형식으로 설정하는 것 중요
"""

# 지도 크기 입력 받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성
d = [[0]*m for _ in range(n)]

# 캐릭터 위치 좌표, 방향 -> direction은 새로 정의한 방향 벡터의 인덱스 역할
x, y, direction = map(int, input().split())

# 지도 모양
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

# 북동남서 방향 벡터 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 게임 시작
count= 1
turn_time= 0

while True:
    # 왼쪽으로 회전
    turn_left()
    # 회전한 방향으로 앞으로 이동
    nx = x + dx(direction)
    ny = y + dy(direction)
    # 회전한 후 정면에 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        # 뒤로 이동
        nx = x - dx(direction)
        ny = y - dy(direction)
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0

print(count)

"""
세 번째 조건: 네 방향 전부 가봤거나 바다이면 뒤로 이동, 그런데 뒤가 바다면 멈춤
지문에서 위 조건을 머리로 받아드리는데 어려움을 겪었다.  
"""
