"""
배열 돌리기 1과 다른 점: R의 횟수 범위

시간 복잡도를 해결하기 위해 회전 시 완벽하게 원 상태로 돌아오는 횟수를 최소 공배수를 이용하여 구한 뒤, (R을 최소공배수로 나눈 나머지) 만큼 시행하면 해결할 것이다.
-> 그래도 시간 초과다. 대략난감.

math.gcd (최대공약수), math.lcm(최소공배수)
"""
import math

n, m, r = map(int, input().split())

x = min(n, m) // 2

y_list = [2*(n+m-2-2*k) for k in range(x)]
y = y_list[0]
# 최소공배수 구하기 -> r번 회전 했을 때 원래 배열로 돌아오는 최소 횟수를 의미.
for i in range(1, len(y_list)): 
    y = math.lcm(y, y_list[i])

# 회전 횟수 r 다시 설정
r1 = r % y

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

for i in range(r1):
    lst = rotate(lst)

for i in range(n):
    for j in range(m):
        print(lst[i][j], end=' ')
    print()
