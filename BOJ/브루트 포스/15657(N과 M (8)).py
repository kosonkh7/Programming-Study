n, m = map(int, input().split())

n_list = list(map(int, input().split()))

from itertools import product

temp = list(product(sorted(n_list), repeat=m))

answer = []

for i in temp:
    x = sorted(i)
    if x in answer:
        answer.append(x)

for i in range(len(answer)):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()


"""
모범답안.
product로 하면 메모리 초과 발생한다. 불필요한 공간 복잡도를 고려해야 하는 문제인가보다.
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return
    for i in range(start, n):
            temp.append(nums[i])
            dfs(i)
            temp.pop()

dfs(0)

"""