import math

t = int(input())

for i in range(t):
    m, n, x, y = map(int, input().split())
    mn = math.lcm(m, n)
    i = 0
    # 정답의 최대값은 m,n의 최소공배수
    while (m * i + x) <= mn:
        # y = a일 때 나머지는 0이게 설정하는 변수 a
        if y == n:
            a = 0
        else: a = y
        if (m * i + x) % n == a:
            break
        else: i += 1
    answer = m * i + x

    if answer > mn:
        print(-1)
    else: print(answer)