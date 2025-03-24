
visited = [False] * 11000

n =  1

while n <= 10000:
    tmpn = n
    tmp = 0
    while tmpn > 0:
        tmp += tmpn % 10
        tmpn //= 10
    visited[tmp + n] = True
    if visited[n] == False:
        print(n)
    n += 1