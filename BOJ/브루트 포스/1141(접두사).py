n = int(input())
n_list = []
for _ in range(n):
    n_list.append(input())
n_list = list(set(n_list))
n_list.sort(key=lambda x: len(x))
n = len(n_list)

answer = len(n_list)
for i in range(n-1):
    is_start = False
    for j in range(i+1, n):
        if n_list[j].startswith(n_list[i]):
            is_start = True
            break
    if is_start:
        answer -= 1

print(answer)