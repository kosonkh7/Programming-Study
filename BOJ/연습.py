n, m = map(int, input().split())
n_list = list(map(int, input().split()))

candy = [i+1 for i in range(n)]
answer = 0

for i in n_list:
    target = candy.index(i)
    if target == 0:
        candy = candy[1:]
    elif target <= len(candy)//2:
        candy = candy[target+1:] + candy[:target]
        answer += target
    elif target == len(candy)-1:
        answer += 1
        candy = candy[:target]
    else:
        candy = candy[target+1:] + candy[:target]
        answer += (len(candy)-target+1)
    #print(candy, answer)
        
print(answer)