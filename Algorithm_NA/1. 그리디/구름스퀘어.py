n = int(input())

n_list = []

for i in range(n):
    n_list.append(list(map(int, input().split())))

# 끝 시간 기준 오름차순 정렬
n_list.sort(key= lambda x : x[1])

def max_count(n_list):
    e = -1
    count = 0
    for i in range(n):
        if e < n_list[i][0]:
            count+= 1
            e =  n_list[i][1]
    return count

print(max_count(n_list))