"""
1인 경우는 시계 방향이고, -1인 경우는 반시계 방향

#x = '10101111'
#x = x[1:]+x[0] # 반시계방향 
#x = x[-1]+x[:7] # 시계방향

deque의 rotate 함수 사용하면 간단하게 회전 가능하다고 한다.
"""

t = int(input()) # 톱니 개수
t_list = [''] # 톱니 순서대로 담을 리스트
for _ in range(t):
    x = input()
    t_list.append(x)

n = int(input()) # 회전 횟수

for _ in range(n):
    k, turn = map(int, input().split()) # 몇 번째 톱니, 회전 방향 입력 받음
    l, r  = k, k # 오른쪽 왼쪽 회전 방향 각각 받기 <- 꼭 필요 없을 듯
    command = [0] * (t+1) # 몇 번째 톱니 어떻게 회전 받나 저장용
    command[k] = turn

    if k < t: 
        while r+1 <= t: # 오른쪽 조회
            if t_list[r][2] == t_list[r+1][6]: # 같은 극이면 조회 중지
                break
            else: # 다른 극이면 회전 방향 저장
                command[r+1] = command[r] * (-1)
                r += 1

    if k > 1: # 왼쪽 조회               
        while l-1 >= 1:
            if t_list[l-1][2] == t_list[l][6]:
                break
            else:
                command[l-1] = command[l] * (-1)
                l -= 1

    for i in range(1, t+1): # 저장된 방향대로 회전시키기
        if command[i] == -1:
            t_list[i] = t_list[i][1:] + t_list[i][0] 
        elif command[i] == 1:
            t_list[i] = t_list[i][-1] + t_list[i][:7]

#print(t_list)

answer = 0
for i in range(t):
    if t_list[i+1][0] == "1":
        answer += 1

print(answer)