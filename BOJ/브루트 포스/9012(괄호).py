t = int(input())
for _ in range(t):
    x = input()
    tmp = x[0]
    for i in range(1, len(x)):
        tmp = tmp + x[i]
        if tmp[-2:] == '()':
            tmp = tmp[:-2]
    if tmp == '':
        print('YES')
    else:
        print('NO')