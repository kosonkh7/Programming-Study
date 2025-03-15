t = int(input())

for i in range(t):
    tmp = list(map(int, input().split()))
    tmp.sort(reverse=True)
    print(tmp[2])