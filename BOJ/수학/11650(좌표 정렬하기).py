n = int(input())

n_list = list(list(map(int, input().split())) for _ in range(n))

answer = sorted(n_list)

for i in range(n):
    print(answer[i][0], answer[i][1])