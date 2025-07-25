s = input()
n_list = []
for i in range(len(s)):
    for j in range(len(s)-i):
        n_list.append(s[j:j+i+1])
n_list = list(set(n_list))
print(len(n_list))