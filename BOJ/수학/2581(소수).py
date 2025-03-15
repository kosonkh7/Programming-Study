m = int(input())
n = int(input())

i = 1
board = [] # 조회 했는지 리스트
prime_list = [] # 소수 리스트

# 에라토스테네스의 체?
while i < n:
    i += 1
    if i not in board:
        prime_list.append(i)
        x = i
        while x <= n:
            board.append(x)
            x += i

board.sort()   

answer_list = []
for a in prime_list:
    if m <= a <= n:
        answer_list.append(a)
    elif a > n:
        break

if len(answer_list) > 0:
    print(sum(answer_list))
    print(min(answer_list))
else:
    print(-1)
