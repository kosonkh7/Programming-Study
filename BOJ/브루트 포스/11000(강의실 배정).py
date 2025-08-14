# 11000 강의실 배정
# 강의 일정을 모두 소화할 수 있는 최소 강의실 개수
# 사례 만들어서 직접 해보면 알고리즘 직관적으로 이해하면서 짜기 좋았다.

import heapq
n = int(input())
n_list = []

for _ in range(n):
    x = list(map(int, input().split()))
    n_list.append(x)

n_list.sort(key=lambda x:[x[0], x[1]])

heap = [n_list[0][1]]
for i in range(1, n):
    if heap[0] <= n_list[i][0]:
        heapq.heappushpop(heap, n_list[i][1])
    else:
        heapq.heappush(heap, n_list[i][1])

print(len(heap))
