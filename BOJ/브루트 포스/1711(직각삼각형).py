# 1711 직각삼각형 - 브루트포스

n = int(input())
n_list = [list(map(int, input().split())) for _ in range(n)]
answer = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = (n_list[i][0] - n_list[j][0])**2 + (n_list[i][1] - n_list[j][1])**2
            b = (n_list[i][0] - n_list[k][0])**2 + (n_list[i][1] - n_list[k][1])**2
            c = (n_list[k][0] - n_list[j][0])**2 + (n_list[k][1] - n_list[j][1])**2
            if a == b + c or b == a + c or c == a + b:
                answer += 1
print(answer)
