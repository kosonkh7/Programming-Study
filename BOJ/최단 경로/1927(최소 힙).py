import heapq

n = int(input())
n_list = [int(input()) for _ in range(n)]
heap = []

for x in n_list:
    if x != 0:
        heapq.heappush(heap, x)
    else:
        try: 
            print(heapq.heappop(heap))
        except:
            print(0)