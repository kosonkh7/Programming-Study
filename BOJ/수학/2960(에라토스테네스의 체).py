n, k = map(int, input().split())

count = 0
visited = [False] * (2500)

answer = 0
start = 2
while start < n:
    if answer > 0:
        break

    if visited[start] == False:
        x = start
        while x <= n:
            if visited[x] == False:
                visited[x] = True
                count += 1

            if count == k:
                answer = x
                break
            x += start

    start += 1

print(answer)