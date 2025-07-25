a, b = input().split()
a_list = list(a)
b_list = list(b)

answer = 100
for i in range(len(b_list)-len(a_list)+1):
    tmp = 0
    for j in range(len(a_list)):
        if a_list[j] != b_list[i+j]:
            tmp += 1
    answer = min(tmp, answer)

print(answer)