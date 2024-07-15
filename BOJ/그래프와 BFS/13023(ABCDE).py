"""
첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.

둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.

DFS로 접근해볼 것
"""

n, m = map(int , input().split())
visited = [False]*(n)
adjacent = [ [] for _ in range(n) ]
arrive = False

for _ in range(m):
    a,b = map(int, input().split())
    adjacent[a].append(b)
    adjacent[b].append(a)

def dfs(start , depth):
    global arrive
    visited[start]=True
    if depth==5:
        arrive = True
        return
    for i in adjacent[start]:
        if visited[i] == False:
            dfs(i , depth+1)
    visited[start]=False

for i in range(n):
    dfs(i ,1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)