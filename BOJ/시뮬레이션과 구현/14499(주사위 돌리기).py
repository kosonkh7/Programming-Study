"""
첫째 줄에 지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)가 주어진다.

둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 각 줄은 서쪽부터 동쪽 순서대로 주어진다. 주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 
지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.

마지막 줄에는 이동하는 명령이 순서대로 주어진다. 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4로 주어진다.

이동할 때마다 주사위의 윗 면에 쓰여 있는 수를 출력한다. 만약 바깥으로 이동시키려고 하는 경우에는 해당 명령을 무시해야 하며, 출력도 하면 안 된다.

1. 지도 밖으로 가면 무시하는 조건
2. 주사위 전개도 참고하여 리스트화 -> 회전 시 모양 고려
3. 0일 때 swap하는 조건 설정
"""

n, m, x, y, K = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(n)]
k_list = list(map(int, input().split()))

dice = [0]*7 

def move(dice, k):
    # 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
    if k == 1:
        dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
    elif k == 2:
        dice[1], dice[3], dice[6], dice[4] = dice[3], dice[6], dice[4], dice[1]
    elif k == 3:
        dice[1], dice[5], dice[6], dice[2] = dice[5], dice[6], dice[2], dice[1]
    elif k == 4:
        dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]
    return dice

for k in k_list:
    # 1. 지도 밖으로 나가면 무시
    if y == 0 and k == 2:
        continue
    if y == m-1 and k == 1:
        continue
    if x == 0 and k == 3:
        continue
    if x == n-1 and k == 4:
        continue
    # 2. 좌표 이동
    if k == 1:
        y += 1
    elif k == 2:
        y -= 1
    elif k == 3:
        x -= 1
    elif k == 4:
        x += 1
    # 3. 주사위 이동
    dice = move(dice, k)
    # 4. 
    if map_[x][y] == 0:
        map_[x][y] = dice[6]
    else:
        dice[6] = map_[x][y]
        map_[x][y] = 0

    print(dice[1])
    

"""
방향벡터 dx, dy 설정해서 k에 따라 적용되도록 설계하면 코드가 더 간결해질 것!

1. nx, ny = x+dx[k], y+dy[k]
2. nx, ny 조건 만족한다면, x,y = nx, ny
"""