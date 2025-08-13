"""
봄 -> 나이 어린 순으로 자기 나이만큼 땅의 양분 소모, 그 뒤에 나이 +1. 양분 없으면 죽음
여름 -> 봄에 죽은 나무의 나이 절반이 해당 땅에 추가 (소수점 아래는 버린다)
가을 -> 나무 나이가 5의 배수면, 인접한 8개 칸에 나이 1인 나무 증식
겨울 -> 땅에 A배열만큼 양분을 추가

사계절을 K년 반복했을 때 나무의 개수


시간 초과 -> tree를 n*n 리스트에 양분으로 저장하면 해결될지도
tree 번식하고 하나 하나씩 heapq로 관리하는 게 시간이 많이 잡아먹나보다.

혹은 인덱스를 적절하게 이용함으로써 관리.
"""
import heapq
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
n_list = [[5]* n for _ in range(n)]
A_list = [list(map(int, input().split())) for _ in range(n)] # 겨울에 추가되는 양분

tree = [] 
dead = [] # 죽은 나무 정보 담을 리스트

for _ in range(m):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    heapq.heappush(tree, (z, x, y))

def spring(tree, n_list, dead):
    tmp = []

    for _ in range(len(tree)):
        z, x, y = heapq.heappop(tree)
        if n_list[x][y] >= z:
            n_list[x][y] -= z
            heapq.heappush(tmp, (z+1, x, y))
        else:
            dead.append((z, x, y))

    tree = tmp
    return tree, n_list, dead 

def summer(tree, n_list, dead):

    for _ in range(len(dead)):
        z, x, y = dead.pop()
        n_list[x][y] += (z // 2)
    
    return tree, n_list, dead

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def autumn(tree):
    for z, x, y  in list(tree):
        if z % 5 == 0:
            for j in range(8):
                nx = x + dx[j]
                ny = y + dy[j]
                if 0 <= nx < n and 0 <= ny < n:
                    heapq.heappush(tree, (1, nx, ny))

    return tree

def winter(n_list):
    for i in range(n):
        for j in range(n):
            n_list[i][j] += A_list[i][j]
    
    return n_list
            
for _ in range(k):
    tree, n_list, dead = spring(tree, n_list, dead)
    tree, n_list, dead = summer(tree, n_list, dead)
    tree = autumn(tree)
    n_list = winter(n_list)

print(len(tree))