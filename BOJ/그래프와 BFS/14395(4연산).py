from collections import deque
s, t = map(int, input().split())

find_answer = False
answer = []
queue = deque([(s, ''), (1, '/'), (0, '-')])
if s != t:
    while queue:
        x, ans = queue.popleft()

        if x == t:
            find_answer = True
            answer.append(ans)

        else:
            if x*x <= t  and x*x != 1 and x*x != 0:
                queue.append([x*x, ans + '*'])

            if x+x <= t  and x+x != 0:
                queue.append([x+x, ans + '+'])      
else:
    find_answer = True
    answer = 0

if not find_answer:
    print(-1)
elif answer == 0:
    print(0)
else:
    answer.sort(key=lambda x: len(x))
    print(answer[0])



















# from collections import deque

# s, t = map(int, input().split())

# visited = [False] * (t + 1)
# visited[s] = True

# answer = -1
# queue = deque([(s, '')])
# if s!= t:
#     while queue:
#         x, ans = queue.popleft()

#         if x == t:
#             answer = ans
#             break

#         if x*x <= t + 1 and not visited[x*x]:
#             visited[x*x] = True
#             queue.append([x*x, ans + '*'])

#         if x+x <= t + 1 and not visited[x+x]:
#             visited[x+x] = True
#             queue.append([x+x, ans + '+'])

#         if not visited[x-x]:
#             visited[x-x] = True
#             queue.append([x-x, ans + '-'])

#         if x!=0 and not visited[1]:
#             visited[1] = True
#             queue.append([1, ans + '/'])
# else:
#     answer = 0

# print(answer)