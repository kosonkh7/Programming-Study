n = int(input())
n_list = list(map(int, input().split()))

table = [2]

# 소수이면 True, 아니면 False
con = True

for i in range(3, 1001):
    for j in table:
        if i % j == 0:
            con = False
            break
    if con == False:
        con = True
    elif con == True:
        table.append(i)


answer = 0

for x in n_list:
    if x in table:
        answer+=1

print(answer)