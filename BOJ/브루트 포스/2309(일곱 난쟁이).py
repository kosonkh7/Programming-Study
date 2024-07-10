

lst = []

for i in range(9):
    lst.append(int(input()))

lst.sort()
sum_ = sum(lst)

# for i in range(8):
#     for j in range(i+1, 9):
#         if lst[i] + lst[j] == sum_-100:
#             x = lst[i]
#             y = lst[j]
#             lst.remove(x)
#             lst.remove(y)
#             break

# for i in lst:
#     print(i)

for i in range(8):
    for j in range(i+1, 9):
        if lst[i] + lst[j] == sum_-100:
            for k in range(9):
                if k==i or k==j:
                    pass
                else:
                    print(lst[k])
                break

