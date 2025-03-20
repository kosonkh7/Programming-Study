h, w = map(int, input().split())
block_list = list(map(int, input().split()))
n_list = [[False]*w for _ in range(h)] # 

for i in range(h):
    for j in range(w):
        if block_list[j]-1 >= i:
            n_list[i][j] = True


# 시뮬레이션
# 왼쪽 벽이 있으면 세기 시작. 오른 쪽 벽을 만나면 그 사이 개수 세어서 answer에 반영
answer = 0
left_wall = False

for i in range(h):
    left_wall = False
    right_wall = False
    tmp = 0
    for j in range(w):
        if not left_wall and n_list[i][j] == True:
            left_wall = True
        
        if left_wall and n_list[i][j] == False:
            tmp += 1
        elif left_wall and n_list[i][j] == True:
            answer += tmp
            tmp = 0

print(answer)