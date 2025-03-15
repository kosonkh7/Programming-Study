a, b = map(int, input().split())

# 수열 만들기
tmp = []
i = 0
while len(tmp) <= 1000:
    i += 1
    for _ in range(i):
        tmp.append(i)

print(sum(tmp[a-1:b]))