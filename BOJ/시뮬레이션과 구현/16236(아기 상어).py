"""
어렵지만 풀었다!

구할 것 -> 최소 몇 초 동안 진행되는지.

공간에 먹을 수 있는 물고기가 없으면 종료

크기가 같으면 지나갈 수만 있음
크기가 작으면 먹을 수 있음
먹을 수 있는 게 1마리면 그 물고기 먹으러 감
먹을 수 있는 게 여럿이면 가장 가까운 거 찾아서
그런데 가까운 게 여럿이면 가장 왼쬑 위에 있는 걸 먹는다.

같은 수의 물고기를 먹을 때마다 크기가 1 증가한다.

# 방법
매 물고기를 찾으러 갈 때마다 타겟을 설정한다. 
타겟 설정 방법 -> 가장 가까운 먹이 찾음. 만약에 같은 거리 먹이 있으면 위-> 왼쪽

먹은 칸은 -1로 설정.
"""
from collections import deque
n = int(input())
n_list = []
x, y = -100, -100 # 시작 위치 (x, y)
age = 2
exp = 0 # 경험치
answer = 0 # 상어가 이동한 거리를 누적해서 더해줄 예정

# 방향벡터
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 시작 위치 찾기
# 시작 위치 찾으면 0으로 초기화
for i in range(n):
    tmp = list(map(int, input().split()))
    n_list.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == 9:
            x = i
            y = j
n_list[x][y] = 0   # <- 이거 안해서 계속 꼬임...ㅠ

# 먹이 찾아가는 함수
def move(x, y): # 입력값 현재 위치 
    global n_list

    visited = [[False]*n for _ in range(n)] # 방문 테이블 매 이동마다 초기화
    queue = deque([[x, y, 0]]) # 큐에 이동 거리 넣어줌
    visited[x][y] = True

    food = [] # 최소 거리 먹이 후보
    food_min = 999999 # 먹이까지 최소 거리

    while queue:
        p, q, dist = queue.popleft()

        for i in range(4):
            np = p + dx[i]
            nq = q + dy[i]
            if 0 <= np < n and 0 <= nq < n and not visited[np][nq]:
                # BFS니까 먹이 찾으면 그 뒤론 큐에 안 넣는 방식
                if 1 <= n_list[np][nq] < age and food_min == 999999 and n_list[np][nq] != 9:
                    food.append([np, nq])
                    food_min = dist + 1
                    visited[np][nq] = True
                elif 1 <= n_list[np][nq] < age and food_min == dist+1 and n_list[np][nq] != 9:
                    food.append([np, nq])
                    visited[np][nq] = True
                elif n_list[np][nq] == 0 or n_list[np][nq] == age:
                    queue.append([np, nq, dist+1])
                    visited[np][nq] = True
    
    food.sort(key=lambda x:[x[0], x[1]])

    if food_min == 999999: # 먹이 못 찾는 경우
        return -100, -100, 999999
    else:
        return food[0][0], food[0][1], food_min

# 레벨 올리기
def levelup(age, exp):
    if age == exp:
        age += 1
        exp = 0
    return age, exp

while True:
    x, y, dist = move(x, y)
    if dist == 999999:
        break
    n_list[x][y] = 0 # 먹은 먹이 초기화
    answer += dist # 계속 이동 거리 더해줌

    exp += 1
    age, exp = levelup(age, exp)

print(answer)  