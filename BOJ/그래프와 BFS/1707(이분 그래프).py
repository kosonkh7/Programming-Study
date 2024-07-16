"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때, 그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
"""

from collections import deque
 
k = int(input())



for _ in range(k):
    n, m = map(int, input().split())
    graph = [[] for x in range(n)]
    visited = [0] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)