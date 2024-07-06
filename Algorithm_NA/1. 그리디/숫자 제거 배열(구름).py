"""
입력값: N과 K | N개의 숫자
출력값: K를 포함하지 않는 숫자의 수
"""

n, k = input().split()
n_list = input().split()

n = int(n)
k_len = len(k)

count = int(n)

for i in range(n):
    if n_list[i].find(k) >= 0:
        count -= 1
        
print(count)