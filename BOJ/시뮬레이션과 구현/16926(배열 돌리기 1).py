n, m, r = map(int, input().split())

x = min(n, m) // 2

lst = [list(map(int, input().split())) for _ in range(n)]

def rotate(lst):
    answer = [[0]*m for _ in range(n)]

    for k in range(x):
        for j in range(k, m-k-1):
            answer[k][j] = lst[k][j+1]

    for k in range(x):
        for i in range(k, n-k-1):
            answer[i+1][k] = lst[i][k]

    for k in range(x):
        for j in range(k, m-k-1):
            answer[n-k-1][j+1] = lst[n-k-1][j]

    for k in range(x):
        for i in range(k, n-k-1):
            answer[n-i-2][m-k-1] = lst[n-i-1][m-k-1] 
    
    return answer

for i in range(r):
    lst = rotate(lst)

for i in range(n):
    for j in range(m):
        print(lst[i][j], end=' ')
    print()