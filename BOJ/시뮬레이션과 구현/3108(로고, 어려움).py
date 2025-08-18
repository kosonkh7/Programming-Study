# 3108 로고, 어려움, 구현
"""
1. 직사각형이 겹쳐있으면 한붓그리기가 가능하다.(점, 선, 면 상관 없음)
2. n이 최대 1000이므로, n**2 조합으로 전부 비교해도 시간 복잡도는 충족
3. 그래프로 서로 연결했는지 확인, 방문 테이블 전부 True로 만들기 위해 반복문 실행 횟수 세면 그게 답

+ 어느 직사각형이 0을 지나는지, 지나지 않는지 확인 필요. (지나면 answer - 1, 처음에 연필은 내리고 있기 때문)
"""
from collections import deque
n = int(input())

contact_zero = False
def pass_zero(lst):
    """
    (0, 0)을 지나는 선분 또는 꼭짓점이 있는지 확인
    """
    if lst[0] == 0 and lst[1] <= 0 and lst[3] >= 0:
        return True
    elif lst[1] == 0 and lst[0] <= 0 and lst[2] >= 0:
        return True
    elif lst[2] == 0 and lst[1] <= 0 and lst[3] >= 0:
        return True
    elif lst[3] == 0 and lst[0] <= 0 and lst[2] >= 0:
        return True

n_list = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    n_list.append(tmp)
    contact_zero = pass_zero(tmp)


def is_overlap(x: list, y: list):
    """
    # 두 직사각형이 만나면 True, 만나지 않으면 False 
    # 만나지 않는 경우는 2가지. 두 직사각형이 아예 따로 있거나, 교점 없이 완전히 들어가있을 때
    """
    if x[2] < y[0] or x[3] < y[1] or y[2] < x[0] or y[3] < x[1]:
        return False
    elif x[2] == y[0] or y[2] == x[0]:
        if x[1] == y[3] or y[1] == x[3]:
            return True
        else:
            return True
    elif x[1] == y[3] or y[1] == x[3]:
        return True
    elif (x[0]<y[0] and x[1]<y[1] and x[2]>y[2] and x[3]>y[3]) or (y[0]<x[0] and y[1]<x[1] and y[2]>x[2] and y[3]>x[3]):
        return False
    else:
        return True

graph = [[] for _ in range(n)]
visited = [False] * (n)

answer = 0
if n == 1:
    answer = 1
else:
    for i in range(n-1):
        for j in range(i+1, n):
            if is_overlap(n_list[i], n_list[j]): # 두 직사각형이 겹치면 그래프에 추가
                graph[i].append(j)
                graph[j].append(i)

    for i in range(n):
        if visited[i]:
            continue

        elif graph[i] == []:
            visited[i] = True
            answer += 1
        
        else:
            queue = deque([i])
            visited[i] = True
            answer += 1

            while queue:
                q = queue.popleft()
                for g in graph[q]:
                    if not visited[g]:
                        visited[g] = True
                        queue.append(g)

if contact_zero:
    answer -= 1

print(answer)