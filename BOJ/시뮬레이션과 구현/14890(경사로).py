"""
줄마다 한 칸씩 조사하면서, 올라가는 방향과 내려가는 방향을 구분하여 규칙을 정의하는 것이 가장 중요했다. <- 처음엔 못함
"""

n, l = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

answer = 0

line1=[] # 어디가 길인지 인덱스 확인용 (실제 구현에 필요 없고 오류 찾을 때 씀)
# 가로줄 확인
for i in range(n):
    ok = True # 조사 중 false면 길 아님.
    cont = 1 # 연속된 칸 개수
    for j in range(n-1):
        if abs(arr[i][j] - arr[i][j+1]) >= 2:
            ok = False
            break   

        elif arr[i][j] == arr[i][j+1]: # 연속된 칸이 같은 높이면 연속(cont) + 1
            cont += 1

        elif arr[i][j] - arr[i][j+1] == -1: # 올라가는 방향
            if cont >= l: # 연속 값이 경사로 길이보다 길 때
                cont = 1 # 연속 값 초기화. 다음 칸 비교
                continue
            else: # 경사로보다 짧으면, 이 줄은 길 아님
                ok = False 
                break     

        elif arr[i][j] - arr[i][j+1] == 1: # 내려가는 방향
            if j+l >= n: # 경사로 설치 전에 길 끝에 도달하면 길 아님.
                ok = False 
                break   
            okok = True # 경사로 설치할 여유가 충분한지 확인하기 위한 변수             
            for k in range(1, l):  
                if arr[i][j+1] == arr[i][j+1+k]: # 현재 칸 이후 L개의 칸이 전부 
                    continue
                else:
                    okok = False
                    break
            if okok == False:
                ok = False 
                break   
            else:
                cont = -l + 1 # 연속된 칸 조사할 때, 이미 경사로 설치된 칸은 빼기 위해 음수로 설정          

    if ok == True: # 길이 맞으면 + 1
        answer += 1
        line1.append(i)


line2=[]
# 세로 줄 확인 (가로줄과 코드 동일, for문 방향만 다르게)
for i in range(n):
    ok = True
    cont = 1
    for j in range(n-1):
        if abs(arr[j][i] - arr[j+1][i]) >= 2:
            ok = False
            break   

        elif arr[j][i] == arr[j+1][i]: # 연속된 칸이 같은 높이면 연속(cont) + 1
            cont += 1

        elif arr[j][i] - arr[j+1][i] == -1: # 올라가는 방향
            if cont >= l: # 연속 값이 경사로 길이보다 길 때
                cont = 1 # 연속 값 초기화. 다음 칸 비교
                continue
            else: # 경사로보다 짧으면, 이 줄은 길 아님
                ok = False 
                break     

        elif arr[j][i] - arr[j+1][i] == 1: # 내려가는 방향
            if j+l >= n:
                ok = False 
                break   
            okok = True              
            for k in range(1, l):  
                if arr[j+1][i] == arr[j+1+k][i]:
                    continue
                else:
                    okok = False
                    break
            if okok == False:
                ok = False 
                break   
            else:
                cont = -l + 1            
                
    if ok == True: # 길이면 + 1
        answer += 1
        line2.append(i)


print(answer)
#print(line1, line2)




















# # 가로 줄
# for i in range(n):
#     ok = True
#     cont = 1
#     updown = 0 
#     for j in range(n-1): # 한 줄씩 조회
#         if arr[i][j] == arr[i][j+1]: # 연속된 칸이 같은 높이면 연속(cont) + 1
#             cont += 1

#         elif arr[i][j] - arr[i][j+1] == 1: # 높이 차이가 1이고 내려가는 방향
#             updown = 1
#             cont = 1
#             # if cont >= l: # 연속 값이 경사로 길이보다 길 때
#             #     cont = 1 # 연속 값 초기화. 다음 칸 비교
#             #     continue
#             # else: # 경사로보다 짧으면, 이 줄은 길 아님
#             #     ok = False 
#             #     break

#         elif arr[i][j] - arr[i][j+1] == -1: # 높이 차이가 1이고 올라가는 방향
#             if updown == 1:
#                 cont -= l  
#             updown = -1
#             if cont >= l: # 연속 값이 경사로 길이보다 길 때
#                 cont = 1 # 연속 값 초기화. 다음 칸 비교
#                 continue
#             else: # 경사로보다 짧으면, 이 줄은 길 아님
#                 ok = False 
#                 break

#         else: # 다음 칸과 차이가 2이상이면 길 아님
#             ok=False
#             break
    
#     if ok == True: # 길이면 + 1
#         answer += 1


# # 조회
# for i in range(n):
#     ok = True
#     cont = 1
#     updown = 0 
#     for j in range(n-1): # 한 줄씩 조회
#         if arr[j][i] == arr[j+1][i]: # 연속된 칸이 같은 높이면 연속(cont) + 1
#             cont += 1
#         elif abs(arr[j][i] - arr[j+1][i]) == 1: # 높이 차이가 1이면,
#             if cont >= l: # 연속 값이 경사로 길이보다 길 때
#                 cont = 0 # 연속 값 초기화. 다음 칸 비교
#                 continue
#             else: # 경사로보다 짧으면, 이 줄은 길 아님
#                 ok = False 
#                 break


#         else: # 다음 칸과 차이가 2이상이면 길 아님
#             ok=False
#             break
    
#     if ok == True: # 길이면 + 1
#         answer += 1


