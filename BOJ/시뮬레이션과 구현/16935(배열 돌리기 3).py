import copy

n, m, r = map(int, input().split())

lst = [list(map(int, input().split())) for _ in range(n)]

a_list = list(map(int, input().split()))

def change(lst, a):
    n = len(lst)
    m = len(lst[0])
    
    if a == 1: # 상하 반전
        answer_list = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                answer_list[n-i-1][j] = lst[i][j]
    elif a == 2: # 좌우 반전
        answer_list = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                answer_list[i][m-1-j] = lst[i][j]
    elif a == 3: # 오른쪽 90도 회전
        answer_list = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                answer_list[j][n-1-i] = lst[i][j]
    elif a == 4: # 왼쪽 90도 회전
        answer_list = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                answer_list[m-1-j][i] = lst[i][j]
    elif a == 5:
        answer_list = [[0]*m for _ in range(n)]
        a1 = [row[:m//2] for row in lst[:n//2]]
        a2 = [row[m//2:] for row in lst[:n//2]]
        a3 = [row[m//2:] for row in lst[n//2:]]
        a4 = [row[:m//2] for row in lst[n//2:]]

        for i in range(n//2): # 1사분면
            for j in range(m//2):
                answer_list[i][j] = a4[i][j]
        for i in range(n//2):
            for j in range(m//2): # 2사분면
                answer_list[i][j+m//2] = a1[i][j]
        for i in range(n//2): # 3사분면
            for j in range(m//2):
                answer_list[i+n//2][j+m//2] = a2[i][j]        
        for i in range(n//2): # 4사분면
            for j in range(m//2):
                answer_list[i+n//2][j] = a3[i][j]      


    elif a == 6:
        answer_list = [[0]*m for _ in range(n)]
        a1 = [row[:m//2] for row in lst[:n//2]]
        a2 = [row[m//2:] for row in lst[:n//2]]
        a3 = [row[m//2:] for row in lst[n//2:]]
        a4 = [row[:m//2] for row in lst[n//2:]]

        for i in range(n//2): # 1사분면
            for j in range(m//2):
                answer_list[i][j] = a2[i][j]
        for i in range(n//2):
            for j in range(m//2): # 2사분면
                answer_list[i][j+m//2] = a3[i][j]
        for i in range(n//2): # 3사분면
            for j in range(m//2):
                answer_list[i+n//2][j+m//2] = a4[i][j]        
        for i in range(n//2): # 4사분면
            for j in range(m//2):
                answer_list[i+n//2][j] = a1[i][j]   

    return answer_list


for a in a_list:
    lst = change(lst, a)

for i in range(len(lst)):
    for j in range(len(lst[0])):
        print(lst[i][j], end=' ')
    print()