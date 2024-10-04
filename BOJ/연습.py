n, m = map(int, input().split())

n_list = []

for i in range(n):
    tmp = list(map(int, input().split()))
    n_list.append(tmp)
    
answer = 0
    
for i in range(n-1):
    for j in range(m-1):
        for k in range(i+1, n):
            for l in range(j+1, m):
                lst = n_list[i:k][j:l]
                total = 0
                for sublist in lst:
                    for num in sublist:
                        total += num
                if total == 10:
                    answer += 1
                    

lst = n_list[0:1][0:1]          
                    
print(n_list)
print(n_list[0])
print(n_list[1])
print(n_list[0:1])
print(n_list[1:2][0:1])


total = 0

for sublist in lst:
    for num in sublist:
        total += num

print(total)