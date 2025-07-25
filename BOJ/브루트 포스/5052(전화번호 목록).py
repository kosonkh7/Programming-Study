"""
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
"""

t = int(input())
for x in range(t):
    n = int(input())
    answer = 'YES'
    n_list = []
    for y in range(n):
        n_list.append(input())
    n_list.sort(key=lambda x:len(x))
    for i in range(n-1):
        for j in range(i+1, n):
            if n_list[j].startswith(n_list[i]):
                answer = 'NO'
                break
        if answer == 'NO':
            break
    print(answer)
        