n = int(input())
n_list = list(map(int, input().split()))
b, c = map(int, input().split())

answer = 0

for i in n_list:
    if i <= b:
        answer += 1
    elif (i-b) % c == 0:
        answer += ((i - b) // c + 1) 
    else:
        answer += ((i - b) // c + 2) 

print(answer)