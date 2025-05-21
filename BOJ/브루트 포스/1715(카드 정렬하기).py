import heapq
n = int(input())
n_list = [int(input()) for _ in range(n)]
answer = 0
if n == 1:
    answer = n_list[0]
elif n == 2:
    answer = sum(n_list)
else:
    heapq.heapify(n_list)
    while len(n_list) >= 2:
        x = heapq.heappop(n_list)
        y = heapq.heappop(n_list)
        answer += (x + y)
        heapq.heappush(n_list, x+y)
print(answer)